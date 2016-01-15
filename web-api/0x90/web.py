from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/count', methods=['GET'])
def calc():
    try:
    	op_input = request.args.get('op')
        value1 = float(request.args.get('value1'))
        value2 = float(request.args.get('value2'))
        if op_input == 'sum':
        	operatior = '+'
        	answer = value1 + value2
        elif op_input == 'minus':
        	operatior = '-'
        	answer = value1 - value2
        elif op_input == 'multiply':
        	operatior = '*'
        	answer = value1 * value2
        elif op_input == 'divide':
        	operatior = '/'
        	answer = value1 / value2
        else:
			return render_template('result.html', error='Operation Not Support')
    	return render_template('result.html', 
    		operatior=operatior, value1=value1, value2=value2, answer=answer)    
    except Exception as err:
        return render_template('result.html', error=err.message)

@app.errorhandler(Exception)
def handle_error(e):
    try:
        if e.code == 404:
            return render_template('result.html', error='Page Not Found')
        else:
            return render_template('result.html')        	
    except:
        return render_template('result.html', error='??')

if __name__ == "__main__":
    #app.debug = True
    app.config['TRAP_HTTP_EXCEPTIONS'] = True
    app.run()
