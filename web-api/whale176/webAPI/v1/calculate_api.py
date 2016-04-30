from __future__ import division
import re
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome! You are able to use the url to calculate sum/minus/multiply/divide with the parameters.'


@app.route('/sum')
def do_sum():
    try:
        v1, v2 = read_args_from_url()
        r = str(v1 + v2)
    except TypeError:
        return 'Missing necessary variables input.', 406
    except ValueError:
        return 'Variables should be integer.', 406
    else:
        return r


@app.route('/minus')
def do_minus():
    try:
        v1, v2 = read_args_from_url()
        r = str(v1 - v2)
    except TypeError:
        return 'Missing necessary variables input.', 406
    except ValueError:
        return 'Variables should be integer.', 406
    else:
        return r


@app.route('/multiply')
def do_multiply():
    try:
        v1, v2 = read_args_from_url()
        r = str(v1 * v2)
    except TypeError:
        return 'Missing necessary variables input.', 406
    except ValueError:
        return 'Variables should be integer.', 406
    else:
        return r


@app.route('/divide')
def do_divide():
    try:
        v1, v2 = read_args_from_url()
        r = str(v1 / v2)
    except TypeError:
        return 'Missing necessary variables input.', 406
    except ValueError:
        return 'Variables should be integer.', 406
    except ZeroDivisionError:
        return 'Value2 could not be zero.', 406
    else:
        return r


'''
1. check value1 and value2 are input. => TypeError
2. validate variables are float or int or neither. => ValueError
'''


def validate_input(variables):
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
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    return validate_input([value1, value2])


if __name__ == '__main__':
    app.run(debug=True)
