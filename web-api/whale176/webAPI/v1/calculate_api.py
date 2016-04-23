from __future__ import division
import re
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome! You are able to use the url to calculate sum/minus/multiply/divide with the parameters.'


@app.route('/sum')
def do_sum():
    v1, v2 = read_args_from_url()
    return str(v1 + v2)


@app.route('/minus')
def do_minus():
    v1, v2 = read_args_from_url()
    return str(v1 - v2)


@app.route('/multiply')
def do_multiply():
    v1, v2 = read_args_from_url()
    return str(v1 * v2)


@app.route('/divide')
def do_divide():
    try:
        v1, v2 = read_args_from_url()
        if type(v1) or type(v2) == 'str':
            raise ValueError
        r = (v1 / v2)
    except ValueError:
        return '[Invalid input] variables should be integer.', 406
    except ZeroDivisionError:
        return '[Invalid input] value2 could not be zero.', 406
    else:
        return str(r)


def validate_input(variables):
    valid_vars = []
    try:
        for var in variables:
            is_float = re.compile(r'((\d+)\.(\d*))')
            is_int = re.compile(r'^(\d*)$')
            if is_float.match(var):
                valid_vars.append(float(var))
            elif is_int.match(var):
                valid_vars.append(int(var))
            else:
                raise ValueError

    except ValueError:
        return '[Invalid input] variables should be integer.', 406
    else:
        return valid_vars


def read_args_from_url():
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    return validate_input([value1, value2])


if __name__ == '__main__':
    app.run(debug=True)
