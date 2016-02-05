from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/sum", methods=["GET"])
def f_sum():
    if request.method == "GET":
        try:
            value1 = request.args.get("value1")
            value2 = request.args.get("value2")
            if value1 == None or value2 == None:
                return "406 Error"
            result = float(value1)+float(value2)
            return str(result)
        except:
            return "406 Error"

@app.route("/minus", methods=["GET"])
def f_minus():
    if request.method == "GET":
        try:
            value1 = request.args.get("value1")
            value2 = request.args.get("value2")
            if value1 == None or value2 == None:
                return "406 Error"
            result = float(value1)-float(value2)
            return str(result)
        except:
            return "406 Error"

@app.route("/multiply", methods=["GET"])
def f_multiply():
    if request.method == "GET":
        try:
            value1 = request.args.get("value1")
            value2 = request.args.get("value2")
            if value1 == None or value2 == None:
                return "406 Error"
            result = float(value1)*float(value2)
            return str(result)
        except:
            return "406 Error"

@app.route("/divide", methods=["GET"])
def f_divide():
    if request.method == "GET":
        try:
            value1 = request.args.get("value1")
            value2 = request.args.get("value2")
            if value1 == None or value2 == None:
                return "406 Error"
            result = float(value1)/float(value2)
            return str(result)
        except:
            return "406 Error"

if __name__ == '__main__':
    app.run()
