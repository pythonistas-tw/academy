from flask import Flask
from flask import request
app = Flask(__name__)



@app.route('/sum', methods = ['GET'])
def csum():
    value1 = float(request.args['value1'])
    value2 = float(request.args['value2'])
    result = value1+ value2
    return str(result)

@app.route('/min', methods = ['GET'])
def cmin():
    value1 = float(request.args['value1'])
    value2 = float(request.args['value2'])
    result = value1 - value2
    return str(result)

@app.route('/mul', methods = ['GET'])
def cmul():
    value1 = float(request.args['value1'])
    value2 = float(request.args['value2'])
    result = value1*value2
    return str(result)

@app.route('/div', methods = ['GET'])
def cdiv():
    value1 = float(request.args['value1'])
    value2 = float(request.args['value2'])
    result = value1/value2
    return str(result)


if __name__ == '__main__':
    app.run(port = 80)
