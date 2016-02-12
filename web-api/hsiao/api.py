from flask import Flask, request, abort

app = Flask(__name__)

def check():
	if request.args.get('value1')==None or request.args.get('value2')==None:
		return True,406
	elif not request.args.get('value1').isdigit() or not request.args.get('value2').isdigit():
		return True,406
	return False, 0

@app.route('/sum',methods=['GET'])
def sum():
	isWrong, status=check()
	if isWrong:
		abort(status)
	else:
		return  str(float(request.args.get('value1'))+float(request.args.get('value2')))

@app.route('/minus',methods=['GET'])
def minus():
	isWrong, status=check()
	if isWrong:
		abort(status)
	else:
	    return  str(float(request.args.get('value1'))-float(request.args.get('value2')))

@app.route('/multiply',methods=['GET'])
def multiply():
	isWrong, status=check()
	if isWrong:
		abort(status)
	else:
		return  str(float(request.args.get('value1'))*float(request.args.get('value2')))

@app.route('/divide',methods=['GET'])
def divide():
	isWrong, status=check()
	if isWrong:
		abort(status)
	else:
		return  str(float(request.args.get('value1'))/float(request.args.get('value2')))


if __name__ == '__main__':
	# uncomment to debug
	# app.debug = True
	app.run()
