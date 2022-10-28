#imports Flask from the package flask
from flask import Flask

#This creates an instance of the Flask object using #our module's name as a parameter.
#Flask uses this to resolve resources

app = Flask(__name__)

#Following line is python decorator.
#Flask uses decorators for URL routing, so this line #of code means that the function directly below it #should be called whenever a user visits the main #root page of our web application.
@app.route("/")

#Following line define a function and returns our #message.
def index():
    return "I am learning Flask"

