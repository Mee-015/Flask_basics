#from file_name import object
from datetime import datetime
from app import app

'''@app.route("/producer")
def producer():
    return "hello producer"'''
from flask import request, send_file

#to make use of functions running on different file from models->user_model
from models.user_model import user_model
obj=user_model()

@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone",methods=["POST"])
def user_addone_controller():
    #print(request.form)
    return obj.user_addone_model(request.form)

@app.route("/user/update",methods=["PUT"])
def user_update_controller():
    #print(request.form)
    return obj.user_update_model(request.form)

@app.route("/user/delete/<id>",methods=["DELETE"])
def user_delete_controller(id):
    #print(request.form)
    return obj.user_delete_model(id)

@app.route("/user/patch/<id>",methods=["PATCH"])
def user_patch_controller(id):
    #print(request.form)
    return obj.user_patch_model(request.form,id)

@app.route("/user/limit/<limit>/page/<page>",methods=["GET"])
def user_pagination_controller(limit,page):
    #print(request.form)
    return obj.user_pagination_model(limit,page)

@app.route("/user/<uid>/upload/avatar",methods=["PUT"])
def user_upload_avatar_controller(uid):
    file=request.files['avatar']
    uniqueFileName=str(datetime.now().timestamp()).replace(".","")
    fileNameSplit=file.filename.split(".")
    ext=fileNameSplit[len(fileNameSplit)-1]
    finalFilePath=f"uploads/{uniqueFileName}.{ext}"
    file.save(finalFilePath)
    return obj.user_upload_avatar_model(uid,finalFilePath)

@app.route("/user/<filename>")
def user_getavatar_controller(filename):
    return send_file(f"uploads/{filename}")

#encrypt other fields except password while sending and the jwt expires after a certain duration
#as the jwt can decrypted but new jwt cannot be formed 
@app.route("/user/login",methods=["POST"])
def user_login_controller():
    return obj.user_login_model(request.form)

