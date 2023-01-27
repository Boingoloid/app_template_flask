from flask import Flask 
from flask import request # can remove if don't use
from flask import render_template

app = Flask(__name__)

# Entering a variable in query string without request package
# http://127.0.0.1:5000/?name=wally   <-- query string
@app.route('/')
@app.route('/<name>')  #Capture value entered as name from query string
def index(name="Boingoloid"): #sets name default value
    return render_template('home/index.html', name=name)
    # return "Hello from {}".format(name)



## Getting other types from url and covering floats and ints
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    context = {'num1':num1, 'num2':num2}
    return render_template("home/add.html", **context) #putting ** means there can be any number of arguments, instead of assigning variables one by one
    # return render_template("home/add.html", num1=num1, num2=num2)

app.run(port=5100,debug=True) #if debug true will reload every change


# -----------------------  REFERENCE


## Entering a variable in query with request global package. 
# def index(name="Treehouse"): #sets name default value
#     name = request.args.get('name', name) #if argument is there, assign to name. Args is like a dictionary
#     return "Hello from {}".format(name)


## Return raw html 
# @app.route('/add/<int:num1>/<int:num2>')
# def add(num1, num2):
#     #return '{} + {} = {}'.format(num1, num2, num1 + num2)
#     return """
#         <!doctype html>
#         <html>
#         <head><title>Adding!</title></head>
#         <body>
#         <h1>{} + {}  = {}</h1>
#         </body>
#         </html>
#     """.format(num1, num2, num1 + num2)



# from flask import redirect,url_for,render_template,request

# app=Flask(__name__)
# @app.route('/',methods=['GET','POST'])
# def home():
#     if request.method=='POST':
#         # Handle POST Request here
#         return render_template('index.html')
#     return render_template('index.html')

# if __name__ == '__main__':
#     #DEBUG is SET to TRUE. CHANGE FOR PROD
#     app.run(port=5000,debug=True)