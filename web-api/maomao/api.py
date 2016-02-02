from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/sum", methods=["GET"])
def f_sum():
    if request.method == "GET":
        try:
            value1 = float(request.args.get("value1", "0"))
            value2 = float(request.args.get("value2", "0"))
            result = value1+value2
            return str(result)
        except Exception as e:
            return "Error: {}".format(str(e))

@app.route("/minus", methods=["GET"])
def f_minus():
    if request.method == "GET":
        try:
            value1 = float(request.args.get("value1", "0"))
            value2 = float(request.args.get("value2", "0"))
            result = value1-value2
            return str(result)
        except Exception as e:
            return "Error: {}".format(str(e))

@app.route("/multiply", methods=["GET"])
def f_multiply():
    if request.method == "GET":
        try:
            value1 = float(request.args.get("value1", "0"))
            value2 = float(request.args.get("value2", "1"))
            result = str(value1*value2)
            return result
        except Exception as e:
            return "Error: {}".format(str(e))

@app.route("/divide", methods=["GET"])
def f_divide():
    if request.method == "GET":
        try:
            value1 = float(request.args.get("value1", "0"))
            value2 = float(request.args.get("value2", "1"))
            result = str(value1/value2)
            return result
        except Exception as e:
            return "Error: {}".format(str(e))

if __name__ == '__main__':
    app.run()
