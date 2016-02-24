from app import app, db, LoginForm
from models import User
from flask import render_template, request, redirect, url_for, jsonify, session, flash

@app.route("/")
def hello():
    return "Hello World"
@app.route("/test_show")
def show():
    return render_template('show.html', op="test" ,value1="1", value2="2", result="3")

@app.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   print "Loging............"
   #if form.validate_on_submit():
   if request.method == 'POST':
      print "submit success "
      user = User.query.filter_by(account=request.form['username']).first()
      #user_list = User.query.all()
      if user:
         print "In db...", user
         #return render_template('hello.html')
         return render_template('hello.html',usedid=user.id,username=user.account)
      else:
         return render_template('login.html', form=form)
   else:
      app.logger.debug(form.errors)
      return render_template('login.html', form=form)

@app.route('/caeatedb')
def caeatedb():
   db.create_all()
   print "create db ...."
   return "Create DB"

@app.route('/dropdb')
def dropdb():
   db.drop_all(bind=None)
   db.session.commit()
   return "DROP DB content"
@app.route('/showdb')
def showdb():
   user_list = User.query.all()
   for row in user_list:
      print row
   return "Show DB content"
@app.route('/testdb')
def testdb():
   #
   admin = User('user1', 'password1')
   guest = User('user2', 'password2')

   db.session.add(admin)
   db.session.add(guest)

   db.session.commit()
   return "TEST DB content"
#------------------------------------------------

   
if __name__ == '__main__':
   app.run(debug=True)
   '''
   admin = User('user1', 'password1')
   guest = User('user2', 'password2')
   db.session.add(admin)
   db.session.add(guest)

   db.session.commit()'''
