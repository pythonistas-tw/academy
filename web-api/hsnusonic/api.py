from __future__ import division
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/sum')
def sum():
  try:
    value1 = float(request.args.get('value1'))
    value2 = float(request.args.get('value2'))
    return str(value1 + value2)
  except:
    abort(406)

@app.route('/minus')
def minus():
  try:
    value1 = float(request.args.get('value1'))
    value2 = float(request.args.get('value2'))
    return str(value1 - value2)
  except:
    abort(406)

@app.route('/multiply')
def multiply():
  try:
    value1 = float(request.args.get('value1'))
    value2 = float(request.args.get('value2'))
    return str(value1 * value2)
  except:
    abort(406)

@app.route('/divide')
def divide():
  try:
    value1 = float(request.args.get('value1'))
    value2 = float(request.args.get('value2'))
    return str(value1 / value2)
  except:
    abort(406)

if __name__ == "__main__":
  app.run()
