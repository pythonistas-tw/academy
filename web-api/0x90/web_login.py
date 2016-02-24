from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import User
from forms import SignupForm
app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/')
@login_required
def HomePage():
    return 'Now You See Me'


@app.route('/hello', methods=['GET'])
@login_required
def hello():
    return render_template('hello.html', username=current_user.account)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('hello'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('hello'))
    form = SignupForm()
    if request.method == 'POST':
        user = form.validate(session)
        if user is None:
            return render_template('login.html', form=form)
        else:
            login_user(user)
            return redirect(url_for('hello'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)


@app.errorhandler(Exception)
def handle_error(e):
    try:
        if e.code == 404:
            return jsonify(status='error', msg='404')
        else:
            return jsonify(status='error', msg=str(e.code))
    except:
        return jsonify(status='error', msg=e.message)

if __name__ == "__main__":
    app.debug = True
    app.config['TRAP_HTTP_EXCEPTIONS'] = True

    Base = declarative_base()
    engine = create_engine("sqlite:///db.sqlite", echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    user_1 = User(account="1@gmail.com", password="1")
    session.add(user_1)
    session.commit()

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"
    login_manager.session_protection = "strong"

    @login_manager.user_loader
    def load_user(user_id):
        return session.query(User).get(user_id)
    app.run()
