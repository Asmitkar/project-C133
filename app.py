#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/home")
def home():
    name = 'Asmit'
    age = 13
    return render_template('index.html',new_name = name, age = age)

@app.route('/father')
def father():
    return 'hello father'

#run the application on local server
app.run()
