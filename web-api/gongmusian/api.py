from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def sum():
    value1 = float(request.args.get('value1'))
    value2 = float(request.args.get('value2'))
    return str(value1 + value2)
"""return type need str()"""

@app.route('/minus', methods=['GET'])
def minus():
    value1 = float(request.args.get('value1'))
    value2 = float(request.args.get('value2'))
    return str(value1 - value2)

@app.route('/multiply', methods=['GET'])
def multiply():
    value1 = float(request.args.get('value1'))
    value2 = float(request.args.get('value2'))
    return str(value1 * value2)

@app.route('/divide', methods=['GET'])
def divide():
    value1 = float(request.args.get('value1'))
    value2 = float(request.args.get('value2'))
    return str(value1 / value2)

if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
