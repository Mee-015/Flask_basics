#from file_name import object
from app import app

@app.route("/producer")
def producer():
    return "hello producer"