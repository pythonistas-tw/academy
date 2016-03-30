from __future__ import division
from pprint import pprint
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome! You are able to use the url to calculate sum/minus/multiply/divide with the parameters.'


@app.route('/sum')
def do_sum():
    values = read_args_from_url()
    v1 = validate_num(values["value1"])
    v2 = validate_num(values["value2"])
    return str(v1 + v2)


@app.route('/minus')
def do_minus():
    values = read_args_from_url()
    v1 = validate_num(values["value1"])
    v2 = validate_num(values["value2"])
    return str(v1 - v2)


@app.route('/multiply')
def do_multiply():
    values = read_args_from_url()
    v1 = validate_num(values["value1"])
    v2 = validate_num(values["value2"])
    return str(v1 * v2)


@app.route('/divide')
def do_divide():
    values = read_args_from_url()
    pprint(values)
    v1 = validate_num(values["value1"])
    v2 = validate_num(values["value2"])
    try:
        r = (v1 / v2)
        return str(r)
    except ZeroDivisionError:
        return '[Invalid input] value2 could not be zero.', 406


def validate_num(var):
    # if type(var) == 'int':
    #     return var
    # elif type(var) == 'float':
    #     return var
    # raise Exception('Invalid number is entered.', 406)
    # pprint(var)
    return var


def read_args_from_url():
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    # pprint(validate_num(value1))
    return {'value1': validate_num(value1), 'value2': validate_num(value2)}


def logger(target, msg=None):
    app.logger.debug('{}:{}'.format(msg, target))


def logger_warning(target, msg=None):
    app.logger.warning('{}:{}'.format(msg, target))


def logger_error(target, msg=None):
    app.logger.error(('{}:{}'.format(msg, target)))


if __name__ == '__main__':
    app.run(debug=True)
