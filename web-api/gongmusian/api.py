from flask import Flask, request, jsonify, abort

def isfloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def check_parameter(param):
    if None in param:
        return False, '406', 'Lose Key'
    elif "" in param:
        return False, '406', 'Lose Value'
    else:
        for x in param:
            if isfloat(x) == False: 
                return False, '406', 'Value Type Error'
                break
    return True, '200', 'OK'

def float_2_dec(number):
    return ("%.2f" %number)

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sum", methods=['GET'])
def sum():
    sum_result = 0
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    param = []
    param.append(value1)
    param.append(value2)
    chk, status, error_msg = check_parameter(param)
    if chk:
        sum_result = float_2_dec(float(value1) + float(value2))
        return jsonify(sum=sum_result, status=status)
    else:
        return jsonify(Error= error_msg, status=status)

@app.route("/minus", methods=['GET'])
def minus():
    minus_result = 0
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    param = []
    param.append(value1)
    param.append(value2)
    chk, status, error_msg = check_parameter(param)
    if chk:
        minus_result = float_2_dec(float(value1) - float(value2))
        return jsonify(minus=minus_result, status=status)
    else:
        return jsonify(Error=error_msg, status=status)

@app.route("/multiply", methods=['GET'])
def multiply():
    mul_result = 0
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    param = []
    param.append(value1)
    param.append(value2)
    chk, status, error_msg = check_parameter(param)
    if chk:
        mul_result = float_2_dec(float(value1) * float(value2))
        return jsonify(multiply=mul_result, status=status)
    else:
        return jsonify(Error=error_msg, status=status)

@app.route("/divide", methods=['GET'])
def divide():
    div_result = 0
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    param = []
    param.append(value1)
    param.append(value2)
    chk, status, error_msg = check_parameter(param)
    if chk:
        if float(value2) == 0:
            return jsonify(Error='Value2 shold not be zero!', status='200')
        else:
            div_result = float_2_dec(float(value1) / float(value2))
            return jsonify(divide=div_result, status=status)
    else:
        return jsonify(Error=error_msg, status=status)

@app.errorhandler(404)
def page_no_found(e):
    return jsonify(Error='Page No Found', status='400')

if __name__ == "__main__":
    app.run(debug = True)

