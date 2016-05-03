import re
from flask import request, render_template, redirect, url_for, session
from app import app, db
from .forms import RegistrationForm, SigninForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    # return 'Welcome! You are able to use the url to calculate sum/minus/multiply/divide with the parameters.'
    if 'username' not in session:
        return redirect(url_for('signin'))
    user = {'username': session['username']}
    return render_template("index.html", user=user)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('signin.html', form=form)
        else:
            session['username'] = form.username.data
            return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('signin.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.username.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            session['username'] = newuser.username
            return redirect(request.args.get('next') or url_for('index'))

    elif request.method == 'GET':
        return render_template('signup.html', title='Register', form=form)


@app.route('/signout')
def signout():
    if 'username' not in session:
        return redirect(url_for('signin'))
    session.pop('username', None)
    return redirect(url_for('index'))


# @app.route('/testdb')
# def testdb():
#     if db.session.query("1").from_statement("SELECT 1").all():
#         return 'It works.'
#     else:
#         return 'Something is broken.'


@app.route('/count')
def do_cal():
    error_msg = None
    r = None
    try:
        op, var1, var2 = read_args_from_url()
        v1 = float(var1)
        v2 = float(var2)
        mapping = zip(['sum', 'minus', 'multiply', 'divide'], [v1 + v2, v1 - v2, v1 * v2, v1 / v2])
        for r_op, r_value in mapping:
            if r_op == op:
                r = r_value
                print(r_value)
                break
    except NameError:
        error_msg = 'Undefined operator input.'
    except TypeError:
        error_msg = 'Missing necessary variables input.'
    except ValueError:
        error_msg = 'Variables should be integer.'
    finally:
        return render_template('cal_response.html', responseMsg=r, errMsg=error_msg)


def validate_input(op, *variables):
    if op in ['sum', 'minus', 'multiply', 'divide'] == False:
        raise NameError

    valid_vars = []
    is_float = re.compile(r'((\d+)\.(\d*))')
    is_int = re.compile(r'^(\d*)$')
    for var in variables:
        if var is None:
            raise TypeError

        if is_float.match(var):
            valid_vars.append(float(var))
        elif is_int.match(var):
            valid_vars.append(int(var))
        else:
            raise ValueError
    return valid_vars


def read_args_from_url():
    op = request.args.get('op')
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    validate_input(op, value1, value2)
    return [op, value1, value2]
