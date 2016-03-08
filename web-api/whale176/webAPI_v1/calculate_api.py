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
    v1 = validate_num(values["value1"])
    v2 = validate_num(values["value2"])
    if v2 == 0:
        raise ValueError('[Invalid parameter input] value2 could not be 0.')
    return str(v1 / v2)

def validate_num(var):
    if var is None:
        raise AttributeError('There is no validate parameters entered.')

    if type(var) == 'int' or type(var) == 'float':
        return var
    else:
        s = num(str(var))
        return s

    raise ValueError('[Invalid parameter input] The {} is not a validate number to calculate.'.format(var))
    raise AttributeError('There is no validate number entered.')

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def read_args_from_url():
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    return {'value1': validate_num(value1), 'value2': validate_num(value2)}

def logger(target, msg=None):
    app.logger.debug('{}:{}'.format(msg, target))

def logger_warning(target, msg=None):
    app.logger.warning('{}:{}'.format(msg, target))

def logger_error(target, msg=None):
    app.logger.error(('{}:{}'.format(msg, target)))


if __name__ == '__main__':
    app.run(debug=True)
