from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

def f_sum(value1, value2, v1, v2):
    result = v1+v2
    msg = "The Answer of {} + {} is {}".format(value1, value2, result)
    return render_template('count.html', msg=msg)

def f_minus(value1, value2, v1, v2):
    result = v1-v2
    msg = "The Answer of {} - {} is {}".format(value1, value2, result)
    return render_template('count.html', msg=msg)

def f_multiply(value1, value2, v1, v2):
    result = v1*v2
    msg = "The Answer of {} * {} is {}".format(value1, value2, result)
    return render_template('count.html', msg=msg)

@app.errorhandler(406)
def f_divide(value1, value2, v1, v2):
    try:
        result = v1/v2
        msg = "The Answer of {} / {} is {}".format(value1, value2, result)
        return render_template('count.html', msg=msg)
    except ZeroDivisionError:
        return render_template('count.html', error="Zero Division Error"), 406

operation = {"sum":f_sum, "minus":f_minus, "multiply":f_multiply, "divide":f_divide}

@app.route("/count", methods=["GET"])
@app.errorhandler(406)
def f_count():
    if request.method == "GET":
        try:
            op = request.args.get("op")
            value1 = request.args.get("value1")
            value2 = request.args.get("value2")
            if op == None or op == "" or value1 == None or value1 == "" or value2 == None or value2 == "":
                return render_template('count.html', error="Missing values"), 406
            v1 = float(value1)
            v2 = float(value2)
            return operation[op](value1, value2, v1, v2)
        except ValueError:
            return render_template('count.html', error="Invalid values"), 406
        except:
            return render_template('count.html', error="Unexpected error"), 406

if __name__ == '__main__':
    app.run()