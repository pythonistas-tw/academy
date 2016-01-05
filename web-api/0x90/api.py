from flask import Flask, request, jsonify, abort
from enum import Enum

app = Flask(__name__)

OperatiorEnum = Enum('OperatiorEnum', 'sum minus multiply divide')


def calc(Operatior):
    try:
        value1 = float(request.args.get('value1'))
        value2 = float(request.args.get('value2'))
        if Operatior == OperatiorEnum.sum:
            Ret = str(value1 + value2)
        elif Operatior == OperatiorEnum.minus:
            Ret = str(value1 - value2)
        elif Operatior == OperatiorEnum.multiply:
            Ret = str(value1 * value2)
        elif Operatior == OperatiorEnum.divide:
			Ret = str(value1 / value2)
        else:
			Ret = "error", "Not Support Operatior"
        return  "ok", Ret
    except ValueError as err:
        abort(406, {'errMag': err.message})
    except TypeError as err:
        abort(406, {'errMag': err.message})
    except Exception as err:
        return "error", err.message


@app.route('/')
def HomePage():
    return 'What A Wonderful DAY'


@app.route('/sum', methods=['GET'])
def sumOperation():
    status, data = calc(OperatiorEnum.sum)
    return jsonify(status=status, data=data)


@app.route('/minus', methods=['GET'])
def minusOperation():
    status, data = calc(OperatiorEnum.minus)
    return jsonify(status=status, data=data)


@app.route('/multiply', methods=['GET'])
def multiplyOperation():
    status, data = calc(OperatiorEnum.multiply)
    return jsonify(status=status, data=data)


@app.route('/divide', methods=['GET'])
def divideOperation():
    status, data = calc(OperatiorEnum.divide)
    return jsonify(status=status, data=data)


@app.errorhandler(Exception)
def handle_error(e):
    try:
        if e.code == 404:
            return jsonify(status='error', msg='404')
        elif e.code == 406:
        	return jsonify(status='error', msg='406 ' + e.description['errMag'])
        else:
            return jsonify(status='error', msg=str(e.code))        	
    except:
        return jsonify(status='error', msg='I Cant handle this, Call me') 

if __name__ == "__main__":
    # app.debug = True
    app.config['TRAP_HTTP_EXCEPTIONS'] = True
    app.run()
