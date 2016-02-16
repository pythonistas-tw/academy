from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/sum", methods=["GET"])
def f_sum():
    if request.method == "GET":
        try:
            value1 = request.args.get("value1")
            value2 = request.args.get("value2")
            if value1 == None or value1 == "" or value2 == None or value2 == "":
                return "Missing values", 406
            result = float(value1)+float(value2)
            return str(result)
        except ValueError:
            return "Invalid values", 406
        except:
            return "Unexpected error", 406

@app.route("/minus", methods=["GET"])
def f_minus():
    if request.method == "GET":
        try:
            value1 = request.args.get("value1")
            value2 = request.args.get("value2")
            if value1 == None or value1 == "" or value2 == None or value2 == "":
                return "Missing values", 406
            result = float(value1)-float(value2)
            return str(result)
        except ValueError:
            return "Invalid values", 406
        except:
            return "Unexpected error", 406

@app.route("/multiply", methods=["GET"])
def f_multiply():
    if request.method == "GET":
        try:
            value1 = request.args.get("value1")
            value2 = request.args.get("value2")
            if value1 == None or value1 == "" or value2 == None or value2 == "":
                return "Missing values", 406
            result = float(value1)*float(value2)
            return str(result)
        except ValueError:
            return "Invalid values", 406
        except:
            return "Unexpected error", 406

@app.route("/divide", methods=["GET"])
def f_divide():
    if request.method == "GET":
        try:
            value1 = request.args.get("value1")
            value2 = request.args.get("value2")
            if value1 == None or value1 == "" or value2 == None or value2 == "":
                return "Missing values", 406
            result = float(value1)/float(value2)
            return str(result)
        except ValueError:
            return "Invalid values", 406
        except:
            return "Unexpected error", 406

if __name__ == '__main__':
    app.run()
