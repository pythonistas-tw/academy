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
			Ret = "Not Support Operatior"
        return  Ret
    except ValueError as err:
        abort(406, {'errMag': err.message})
    except Exception as err:
		return err.message


@app.route('/')
def HomePage():
    return 'What A Wonderful DAY'


@app.route('/sum', methods=['GET'])
def sumOperation():
    return jsonify(msg=calc(OperatiorEnum.sum))


@app.route('/minus', methods=['GET'])
def minusOperation():
    return jsonify(msg=calc(OperatiorEnum.minus))


@app.route('/multiply', methods=['GET'])
def multiplyOperation():
    return jsonify(msg=calc(OperatiorEnum.multiply))


@app.route('/divide', methods=['GET'])
def divideOperation():
    return jsonify(msg=calc(OperatiorEnum.divide))


@app.errorhandler(Exception)
def handle_error(e):
    try:
        if e.code == 404:
            return jsonify({'msg': 'Page not Found'})
        elif e.code == 406:
        	return jsonify({'msg': e.description['errMag']})
        else:
            return jsonify({'status': str(e.code)})        	
    except:
        return jsonify({'msg': 'I Cant handle this, Call me'}) 

if __name__ == "__main__":
    #app.debug = True
    app.config['TRAP_HTTP_EXCEPTIONS'] = True
    app.run()