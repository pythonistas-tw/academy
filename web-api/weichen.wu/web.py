from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)
app.debug = True
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/test_show")
def show():
    return render_template('show.html', op="test" ,value1="1", value2="2", result="3")

def check_parameter(value1, value2):
  if value1 == None or value2==None:
    return False, '406', 'Error' 
  else:
    if value1 == "" or value2== "":
      return False, '406', 'Error' 
    elif isfloat(value1)==False or isfloat(value2)==False:
      return False, '406', 'Error' 
  return True, '200', 'OK' 

def isfloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False
#------------------------------------------------

    
@app.route("/count", methods=['GET', 'POST'])
def count():
    op = request.args.get('op')
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    result = clacul(op, value1, value2)
    if result.find("Error") >= 0:
      return result
    else:
      return render_template('show.html', op=op ,value1=value1, value2=value2, result=result)

#------------------------------------------------
def clacul(op, value1, value2):
    if op == "sum":
      return summation(value1, value2)
    elif op == "minus":
      return minus(value1, value2)
    elif op == "multiply":
      return multiply(value1, value2)
    elif op == "divide":
      return divide(value1, value2)
    else:
      return None
def summation(value1, value2):
    sum_result = 0
    chk, status, msg = check_parameter(value1, value2)
    if chk:
        sum_result = float(value1) + float(value2)
    else:
        return status +' '+msg
    sum_result = ("%0.2f" %sum_result)
    return str(sum_result)

def minus(value1, value2):
  chk, status, msg = check_parameter(value1, value2)
  if chk:
    minus_result = float(value1) - float(value2)
  else:
    return status +' '+msg
  minus_result = ("%.2f" %minus_result)
  return str(minus_result)

def multiply(value1, value2):
  mul_result = 0
  chk, status, msg = check_parameter(value1, value2)
  if chk:
    mul_result = float(value1) * float(value2)
  else:
    return status +' '+msg

  mul_result = ("%.2f" %mul_result)
  return str(mul_result)

def divide(value1, value2):
  div_result = 0
  chk, status, msg = check_parameter(value1, value2)
  if chk:
    if float(value2) == 0:
      return "No zero divisor!!"
    else:
      div_result = float(value1) / float(value2)
  else:
    return status +' '+msg
  div_result = ("%.2f" %div_result)
  return str(div_result)
#-----------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)