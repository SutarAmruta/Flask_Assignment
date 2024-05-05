from model.User_Model import usermodel
from flask import request
from app import app

user_obj = usermodel()

@app.route("/user/getall")
def user_getall_controller():
    return user_obj.user_getall_model()

@app.route("/user/add",methods=["post"])
def user_add_controller():
    return user_obj.user_add_model(request.form)

@app.route("/user/update",methods=["put"])
def user_update_controller():
    return user_obj.user_update_model(request.form)

@app.route("/user/delete",methods=["delete"])
def user_delete_controller():
    return user_obj.user_delete_model(request.form)