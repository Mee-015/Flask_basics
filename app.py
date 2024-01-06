from flask import Flask 
app=Flask(__name__)

#to write in same file
@app.route("/")
def welcome():
    return "hello world"
@app.route("/home")
def home():
    return "This is home page"
#we have to import all the files by commas which will increase the length when more no of files are created
#from controller import user_controller

#multiple files
#from controller import user_controller,pro_controller

#can be done in better way using separate file(__init__.py)
from controller import *