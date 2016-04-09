from flask import Flask, request, jsonify, abort, render_template

def isfloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def check_parameter(param, op):
    msg = []
    if op not in ['sum', 'minus', 'multiply', 'divide']:
        msg.append('Operation is not availabe')
    if None in param:
        msg.append('Lose key')
    if '' in param:
        msg.append('Lose Value')
    for x in param:
        # float() need string or number not None
        if x != None and x != '':
            if isfloat(x) == False:
                msg.append('Value Type Error')
    if len(msg) > 0:
        # list to str
        return False, 406, str(msg)[1:-1]
    else:
        return True, 200, 'OK'

def float_2_dec(number):
    return ('%.2f' %number)

app = Flask(__name__)
@app.route('/')
def hello(name = None):
    return render_template('hello.html', name=name)


@app.route('/count', methods=['GET'])
def count():
    op = request.args.get('op')
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    param = []
    param.append(value1)
    param.append(value2)
    chk, status, error_msg = check_parameter(param, op)
    if chk:
        if op == 'sum':
            return render_template('count.html', status=status, value1=value1, op='+', value2=value2, answer=float_2_dec(float(value1) + float(value2)), msg=error_msg)
        elif op == 'minus':
            return render_template('count.html', status=status, value1=value1, op='-', value2=value2, answer=float_2_dec(float(value1) - float(value2)), msg=error_msg)
        elif op == 'multiply':
            return render_template('count.html', status=status, value1=value1, op='×', value2=value2, answer=float_2_dec(float(value1) * float(value2)), msg=error_msg)
        elif op == 'divide':
            if float(value2) == 0:
                return render_template('count.html', status=status, value1=value1, op='÷', value2=value2, answer=" value2 can not equal 0", error_msg=error_msg)
            else:
                return render_template('count.html', status=status, value1=value1, op='÷', value2=value2, answer=float_2_dec(float(value1) / float(value2)), error_msg=error_msg)
    else:
       return render_template('count.html', msg=error_msg)

@app.errorhandler(404)
def page_no_found(e):
    return jsonify(Error='Page No Found', status=404)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8080)
    # setting host='0.0.0.0' and port=8080 running on cloud9

