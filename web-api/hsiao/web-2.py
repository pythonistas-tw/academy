from flask import Flask, request, redirect, url_for, render_template, g
import flask.ext.login as flask_login
import sqlite3
import hashlib


app = Flask(__name__)
app.secret_key = 'super secret string'  # Change this!
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

DATABASE = 'db.sqlite'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()




class User(flask_login.UserMixin):
     pass

@login_manager.user_loader
def load_user(email):
	cur = get_db().cursor()
	if email not in cur.execute('SELECT account FROM User').fetchall():
		return

	user = User()
	user.id = email
	return user

@login_manager.request_loader
def request_loader(request):
	cur = get_db().cursor()
	email = request.form['email']
	if email not in cur.execute('SELECT account FROM User').fetchall():
		return
	
	user = User()
	user.id = email
	password = hashlib.sha1(request.form['pw'].encode('utf-8')).hexdigest()
    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
	if cur.execute('SELECT password FROM User WHERE account="'+ email +'" AND '+'password="'+password+'"').fetchall()==[]:
		user.is_authenticated = False
	else:
		user.is_authenticated = True
	return user

@app.route('/hello',methods=['GET'])
def hello():
	if flask_login.current_user.is_authenticated:
		return render_template('hello.html', user=flask_login.current_user.id)
	else:
		return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	cur = get_db().cursor()
	if request.method == 'GET':
		return '''
			<form action='login' method='POST'>
				<input type='text' name='email' id='email' placeholder='email'></input>
				<input type='password' name='pw' id='pw' placeholder='password'></input>
				<input type='submit' name='submit'></input>
			</form>
               '''
	email = request.form['email']
	password=hashlib.sha1(request.form['pw'].encode('utf-8')).hexdigest()
	if cur.execute('SELECT account,password FROM User WHERE account="'+email+'" AND password="'+password+'"').fetchall()!=[]:
		user = User()
		user.id = email
		flask_login.login_user(user,force=False)
		flask_login.current_user=user
		return redirect(url_for('hello'))
	else:
		return 'Bad login'

@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

if __name__ == '__main__':
	# uncomment to debug
	# app.debug = True
	app.run()

