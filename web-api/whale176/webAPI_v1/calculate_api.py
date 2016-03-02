from flask import Flask, request
import sys

app = Flask(__name__)


# http://127.0.0.1/sum?value1=1&value2=1

@app.route('/')
def index():
    return 'Index Page'

@app.route('/sum')
def do_sum():
    try:
        value1 = request.args.get('value1')
        value2 = request.args.get('value2')
        return str(validate_num(value1) + validate_num(value2))
    except (TypeError, ValueError) as e:
        return str(e)


def validate_num(var):
    if var.isnumeric() is False:
        raise ValueError('The {} is not a number.'.format(var))
    return var

def logger(target):
    return app.logger.debug(target)

# @app.route('/minus')
# def calcul_minus():
#     return 'Hello World'

# @app.route('/multiply')
# def calcul_multiply():
#     return 'Hello World'

# @app.route('/divide')
# def calcul_divide():
#     return 'Hello World'

# def get_values_parameters():
#     val01 = request.args.get('value1')
#     val02 = request.args.get('value2')
#     return (val01, val02)




# def validate_two_parameters():
#     if len(sys.argv) !== 2 :
#         pstderr("We need 2 interger numbers to calculate.")
#         sys.exit(1)

# def main():
# with app.test_request_context():
#     validate_two_parameters()

#     val01 = sys.argv[1]
#     val02 = sys.argv[2]

#     print url_for('index')
#     print url_for('login')
#     print url_for('login', value1=val01, value2=val02)
#     print url_for('profile', username='John Doe')



if __name__ == '__main__':
    app.run(debug=True)
