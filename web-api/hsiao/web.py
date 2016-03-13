from flask import Flask, request, render_template

app = Flask(__name__)

def check():
	if request.args.get("value1")==None or request.args.get('value2')==None or request.args.get("op")==None:
		return True,406
	if request.args.get("op") not in ["sum","minus","multiply","divide"]:
		return True,406
	elif not request.args.get("value1").isdigit() or not request.args.get("value2").isdigit():
		return True,406
	return False, 0

@app.route('/count',methods=['GET'])
def simple_arithmatic():
	isWrong, status=check()
	if isWrong:
		abort(status)
	else:
		if request.args.get("op")=="sum":
			return render_template('answer.html', op="+",
			value1=request.args.get("value1"),
			value2=request.args.get("value2"),
			value3=str(float(request.args.get("value1"))+float(request.args.get("value2"))))
		elif request.args.get("op")=="minus":
			return render_template('answer.html', op="-",
			value1=request.args.get("value1"),
			value2=request.args.get("value2"),
			value3=str(float(request.args.get("value1"))-float(request.args.get("value2"))))
		elif request.args.get("op")=="multiply":
			return render_template('answer.html', op="*",
			value1=request.args.get("value1"),
			value2=request.args.get("value2"),
			value3=str(float(request.args.get("value1"))*float(request.args.get("value2"))))
		elif request.args.get("op")=="divide":
			return render_template('answer.html', op="/",
			value1=request.args.get("value1"),
			value2=request.args.get("value2"),
			value3=str(float(request.args.get("value1"))/float(request.args.get("value2"))))
		else: 
			abort(404)

if __name__ == '__main__':
	# uncomment to debug
	# app.debug = True
	app.run()