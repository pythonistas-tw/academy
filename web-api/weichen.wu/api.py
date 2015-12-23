from flask import Flask
from flask import request
def isfloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "Hello World!"
def check_parameter(value1, value2):
	print "value1:", value1, " value2:", value2
	print "Type:", type(value1)," " ,type(value2)

	if value1 == None or value2==None:
		return False, " 406 Not Acceptable"
	else:
		if value1 == "" or value2== "":
			return False, " 406 Not Acceptable"
		elif isfloat(value1)==False or isfloat(value2)==False:
			return False, " 406 Not Acceptable"
	return True, "OK"
@app.route("/sum", methods=['GET', 'POST'])
def sum():
	sum_result = 0
	value1 = request.args.get('value1')
	value2 = request.args.get('value2')
	chk, status_msg = check_parameter(value1, value2)
	if chk:
		sum_result = float(value1) + float(value2)
	else:
		return status_msg
	sum_result = ("%.2f" %sum_result)
	print "SUM: ", sum_result
	return str(sum_result)

@app.route("/minus", methods=['GET', 'POST'])
def minus():
	minus_result = 0
	value1 = request.args.get('value1')
	value2 = request.args.get('value2')
	chk, status_msg = check_parameter(value1, value2)
	if chk:
		minus_result = float(value1) - float(value2)
	else:
		return status_msg

	minus_result = ("%.2f" %minus_result)
	print "MINUS: ", minus_result
	return str(minus_result)

@app.route("/multiply", methods=['GET', 'POST'])
def multiply():
	mul_result = 0
	value1 = request.args.get('value1')
	value2 = request.args.get('value2')
	chk, status_msg = check_parameter(value1, value2)
	if chk:
		mul_result = float(value1) * float(value2)
	else:
		return status_msg

	mul_result = ("%.2f" %mul_result)
	print "MULTIPLY: ", mul_result
	return str(mul_result)

@app.route("/divide", methods=['GET', 'POST'])
def divide():
	div_result = 0
	value1 = request.args.get('value1')
	value2 = request.args.get('value2')
	chk, status_msg = check_parameter(value1, value2)
	if chk:
		if float(value2) == 0:
			return "No zero divisor!!"
		else:
			div_result = float(value1) / float(value2)
	else:
		return status_msg

	div_result = ("%.2f" %div_result)
	print "DIVIDE: ", div_result
	return str(div_result)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888)

