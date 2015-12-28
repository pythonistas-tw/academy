from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/sum',methods=['GET'])
def sum():
    return  str(float(request.args.get('value1'))+float(request.args.get('value2')))

@app.route('/minus',methods=['GET'])
def minus():
    return  str(float(request.args.get('value1'))-float(request.args.get('value2')))

@app.route('/multiply',methods=['GET'])
def multiply():
    return  str(float(request.args.get('value1'))*float(request.args.get('value2')))

@app.route('/divide',methods=['GET'])
def divide():
    return  str(float(request.args.get('value1'))/float(request.args.get('value2')))

if __name__ == '__main__':
    app.run()
