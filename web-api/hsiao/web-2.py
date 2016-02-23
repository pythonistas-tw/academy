from flask import Flask, request, redirect, url_for, render_template
import flask.ext.login as flask_login

app = Flask(__name__)
app.secret_key = 'super secret string'  # Change this!
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

users = {'foo@bar.tld': {'pw': 'secret'}}

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def load_user(email):
	if email not in users:
		return
	user = User()
	user.id = email
	return user

@login_manager.request_loader
def request_loader(request):
	email = request.form.get('email')
	if email not in users:
		return

	user = User()
	user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
	user.is_authenticated = request.form['pw'] == users[email]['pw']

	return user

@app.route('/hello',methods=['GET'])
def hello():
	return '''
			<h1>Success</h1>
           '''

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return '''
			<form action='login' method='POST'>
				<input type='text' name='email' id='email' placeholder='email'></input>
				<input type='password' name='pw' id='pw' placeholder='password'></input>
				<input type='submit' name='submit'></input>
			</form>
               '''
	email = request.form['email']
	if request.form['pw'] == users[email]['pw']:
		user = User()
		user.id = email
		flask_login.login_user(user)
		return redirect(url_for('hello'))

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
	app.debug = True
	app.run()

