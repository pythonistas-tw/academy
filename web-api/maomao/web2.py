from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask.ext.login import current_user
from flask.ext.login import LoginManager
from flask.ext.login import login_user
from flask.ext.login import logout_user
from flask.ext.login import login_required
from models import User
from models import DBUse
from forms import LoginForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return DBUse().f_read(uid=int(user_id))

@app.route("/home")
def home():
    return "Home Page."

@app.route("/hello")
@login_required
def hello():
    return "Hello, {}!".format(current_user.account)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = []
    if request.method == "POST":
        form = LoginForm(account=request.form["account"], password=request.form["password"])
        if form.is_valid():
            user = DBUse().f_login(account=request.form["account"], password=request.form["password"])
            if user:
                login_user(user)
                next = request.args.get('next')
                return redirect(next or url_for("hello"))
        error.append("Login Failed.")
    else:
        form = LoginForm()
    return render_template('login.html', form=form, current_user=current_user, error=error)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.config["SECRET_KEY"] = "MAOMAOSECRET"
    app.run()