
from flask import Flask, jsonify, request, render_template,redirect
import json

# from numpy.core.arrayprint import printoptions
# from data_input import data_in
import numpy as np
import pickle
from flask_cors import CORS
from flask import jsonify
from flask import request,json
from pymongo import MongoClient
from bson.objectid import ObjectId

title = "sample application with Flask and MongoDB"
heading = "Elastic"

client = MongoClient("mongodb://Thamadie:test@test-shard-00-00.an6bk.mongodb.net:27017,test-shard-00-01.an6bk.mongodb.net:27017,test-shard-00-02.an6bk.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-xhe6nj-shard-0&authSource=admin&retryWrites=true&w=majority") #host uri
db = client.elasticdatabase    #Select the database

def load_models():
    file_name = "models/model_total.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

def load_modelsJac():
    file_name = "models/model_jac.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model
def load_modelsknt():
    file_name = "models/model_knt.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model
def load_modelspk():
    file_name = "models/model_pk.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model
def load_modelsqa():
    file_name = "models/model_qa.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model
def load_modelswev():
    file_name = "models/model_wev.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model
def load_modelsWP():
    file_name = "models/model_WP.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model
def load_modelsdye():
    file_name = "models/model_dye.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)
CORS(app)

#login-start
@app.route("/login", methods=['POST'])
def login():
    request_data=json.loads(request.data)
    print(request_data)
    
    response1=""
    if request_data["username"] != 'admin123' or request_data["password"] != 'admin123':
        response1="password or username is wrong"
    else:
        response1="successfull"

    response = json.dumps({"id": 1,
    "response": response1})
    
    return response
# def login():
#     request_data=json.loads(request.data)
#     print(request_data)
#     # error = None
#     # if request.method == 'POST':
#     #     if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#     #         error = 'Invalid Credentials. Please try again.'
#     #     else:
#     #         return redirect("/")
#     # return render_template('FormSignup.js', error=error)
    

# #login-end

@app.route('/predict', methods=['GET'])
def predict():
    # stub input features
    # request_json = request.get_json()
    # x = request_json['input']

    ata_in=[22979.2965442723, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    x_in =np.array(ata_in).reshape(1,-1)
    # load model
    model = load_models()
    prediction = model.predict(x_in)[0]
    # response = json.dumps({'response': prediction})
    response = json.dumps([{"id": 1,
    "response": prediction}])
    
    return response

@app.route('/elastic', methods=['GET'])
def data():
    # GET all data from database
        allData = db['elastic'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            JobNo = data['JobNo']
            ItemCode = data['ItemCode']
            ColorGroup = data['ColorGroup']
            Total_Quantity = data['Total_Quantity']
            Total_Wastage = data['Total_Wastage']
            waste_pecentage = data['waste_pecentage']

            dataDict = {
                'id': str(id),
                'JobNo': JobNo,
                'ItemCode': ItemCode,
                'ColorGroup': ColorGroup,
                'Total_Quantity': Total_Quantity,
                'Total_Wastage': Total_Wastage,
                'waste_pecentage': waste_pecentage

            }
            dataJson.append(dataDict)
        # print(dataJson)
        return jsonify(dataJson)

@app.route('/sendData',methods=['POST'])
def create():
    request_data=json.loads(request.data)
    print(request_data)


    
    ata_in=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ata_in[0] = request_data["quantity"]
    q=float(request_data["quantity"])

    print(ata_in[0])
    if(request_data["color"]=="DYE_SG_WH"):
        ata_in[-1] = 1.0
    
    if(request_data["color"]=="DYE_SG_MD"):
        ata_in[-2] = 1.0

    if(request_data["color"]=="DYE_SG_LT"):
        ata_in[-3] = 1.0

    if(request_data["color"]=="DYE_SG_FI"):
        ata_in[-4] = 1.0

    if(request_data["color"]=="DYE_SG_DK"):
        ata_in[-5] = 1.0

    if(request_data["color"]=="DYE_SG_BK"):
        ata_in[-6] = 1.0

    


    if(request_data["type"]=="FJ101980-032.0"):
        print(1)
        ata_in[1] = 1.0

    if(request_data["type"]=="FJ103791-032.0"):
        ata_in[2] = 1.0

    if(request_data["type"]=="FJ103880-032.0WH"):
        ata_in[3] = 1.0

    if(request_data["type"]=="FK048204-008.5"):
        ata_in[4] = 1.0

    if(request_data["type"]=="FK048204-008.5BK-1142"):
        ata_in[5] = 1.0

    if(request_data["type"]=="FK048204-008.5BL-0857"):
        ata_in[6] = 1.0

    if(request_data["type"]=="FK048204-008.5BM-1441"):
        ata_in[7] = 1.0

    if(request_data["type"]=="FK048204-008.5BP-1373"):
        ata_in[8] = 1.0

    if(request_data["type"]=="FK048204-008.5CC-1385"):
        ata_in[9] = 1.0

    if(request_data["type"]=="FK048204-008.5CD-1340"):
        ata_in[10] = 1.0

    if(request_data["type"]=="FK048204-008.5FP-0820"):
        ata_in[11] = 1.0

    if(request_data["type"]=="FK048204-008.5LM-0923"):
        ata_in[12] = 1.0

    if(request_data["type"]=="FK048204-008.5MP-1400"):
        ata_in[13] = 1.0

    if(request_data["type"]=="FK048204-008.5MP-1408"):
        ata_in[14] = 1.0

    if(request_data["type"]=="FK048204-008.5PL-0926"):
        ata_in[15] = 1.0

    if(request_data["type"]=="FK048204-008.5SG-1407"):
        ata_in[16] = 1.0

    if(request_data["type"]=="FK048204-008.5SN-1383"):
        ata_in[17] = 1.0

    if(request_data["type"]=="FK048204-008.5WH-0834"):
        ata_in[18] = 1.0

    if(request_data["type"]=="FK048204-008.5WH-1039"):
        ata_in[19] = 1.0

    if(request_data["type"]=="FK054594-015"):
        ata_in[20] = 1.0

    if(request_data["type"]=="FK054595-008"):
        ata_in[21] = 1.0

    if(request_data["type"]=="FK380002-007BK-0231"):
        ata_in[22] = 1.0

    if(request_data["type"]=="FK380002-007BK-1200"):
        ata_in[23] = 1.0

    if(request_data["type"]=="FK380028-008"):
        ata_in[24] = 1.0

    if(request_data["type"]=="FK380028-008(15G)"):
        ata_in[25] = 1.0

    if(request_data["type"]=="FK380028-008BK-0042"):
        ata_in[26] = 1.0

    if(request_data["type"]=="FK380028-008BS-0043"):
        ata_in[27] = 1.0

    if(request_data["type"]=="FK380028-008CR-0044"):
        ata_in[28] = 1.0

    if(request_data["type"]=="FK380028-008GA-0046"):
        ata_in[29] = 1.0

    if(request_data["type"]=="FK380028-008MK-0277"):
        ata_in[30] = 1.0

    if(request_data["type"]=="FK380028-008NI-0050"):
        ata_in[31] = 1.0

    if(request_data["type"]=="FK380028-008PL-0054"):
        ata_in[32] = 1.0

    if(request_data["type"]=="FK380028-008PP-0055"):
        ata_in[33] = 1.0

    if(request_data["type"]=="FK380028-008RW-0056"):
        ata_in[34] = 1.0

    if(request_data["type"]=="FK380028-008SD-0057"):
        ata_in[35] = 1.0

    if(request_data["type"]=="FK380028-008SP-0058"):
        ata_in[36] = 1.0

    if(request_data["type"]=="FK380028-008TA-0059"):
        ata_in[37] = 1.0

    if(request_data["type"]=="FK380028-008WH-0061"):
        ata_in[38] = 1.0

    if(request_data["type"]=="FK380038-011BK"):
        ata_in[39] = 1.0

    if(request_data["type"]=="FK380038-011BK/GR"):
        ata_in[40] = 1.0

    if(request_data["type"]=="FK380038-011SD"):
        ata_in[41] = 1.0

    if(request_data["type"]=="FK380051-056BK/CT"):
        ata_in[42] = 1.0

    if(request_data["type"]=="FK380051-058BK/CT"):
        ata_in[43] = 1.0

    if(request_data["type"]=="FK380051-058SD/CT"):
        ata_in[44] = 1.0

    if(request_data["type"]=="FK380052-008"):
        ata_in[45] = 1.0

    if(request_data["type"]=="FK380052-008WH-0070"):
        ata_in[46] = 1.0

    if(request_data["type"]=="FK380075-025SD"):
        ata_in[47] = 1.0

    if(request_data["type"]=="FK380078-08.5BK-0250"):
        ata_in[48] = 1.0

    if(request_data["type"]=="FK380087-032BK"):
        ata_in[49] = 1.0

    if(request_data["type"]=="FK380087-032SD/CT"):
        ata_in[50] = 1.0

    if(request_data["type"]=="FK380111-006BK/CT"):
        ata_in[51] = 1.0

    if(request_data["type"]=="FK380111-006SD/CT"):
        ata_in[52] = 1.0

    if(request_data["type"]=="FK380112-006SD"):
        ata_in[53] = 1.0

    if(request_data["type"]=="FK380120-022BK/CT"):
        ata_in[54] = 1.0

    if(request_data["type"]=="FK380120-022SD/CT"):
        ata_in[55] = 1.0

    if(request_data["type"]=="FK380120-029BK/CT"):
        ata_in[56] = 1.0

    if(request_data["type"]=="FK380120-029SD/CT"):
        ata_in[57] = 1.0

    if(request_data["type"]=="FK380120-029SD/CT/GR"):
        ata_in[58] = 1.0

    if(request_data["type"]=="FK380120-083SD/GR"):
        ata_in[59] = 1.0

    if(request_data["type"]=="FK380122-025SD"):
        ata_in[60] = 1.0

    if(request_data["type"]=="FK380212-010"):
        ata_in[61] = 1.0

    if(request_data["type"]=="FK380212-010WH-0834"):
        ata_in[62] = 1.0

    if(request_data["type"]=="FK380239-003SD"):
        ata_in[63] = 1.0

    if(request_data["type"]=="FK380334-010.5"):
        ata_in[64] = 1.0

    if(request_data["type"]=="FK380334-010.5SG-1061"):
        ata_in[65] = 1.0

    if(request_data["type"]=="FK380334-010.5WH-1041"):
        ata_in[66] = 1.0

    if(request_data["type"]=="FK380504-008BK"):
        ata_in[67] = 1.0

    if(request_data["type"]=="FK380504-008SD"):
        ata_in[68] = 1.0

    if(request_data["type"]=="FK380617-004WH-1704"):
        ata_in[69] = 1.0

    if(request_data["type"]=="FK380642-012BK"):
        ata_in[70] = 1.0

    if(request_data["type"]=="FW002007-004"):
        ata_in[71] = 1.0

    if(request_data["type"]=="FW002007-004BK-1092"):
        ata_in[72] = 1.0

    if(request_data["type"]=="FW002007-004MG-1093"):
        ata_in[73] = 1.0

    if(request_data["type"]=="FW002007-004WH-1095"):
        ata_in[74] = 1.0

    if(request_data["type"]=="FW002007-006BK-1092"):
        ata_in[75] = 1.0

    if(request_data["type"]=="FW002007-006MG-1093"):
        ata_in[76] = 1.0

    if(request_data["type"]=="FW002007-006WH-1095"):
        ata_in[77] = 1.0

    if(request_data["type"]=="FW051849-007.5"):
        ata_in[78] = 1.0

    if(request_data["type"]=="FW101426-017.0"):
        ata_in[79] = 1.0

    if(request_data["type"]=="FW380006-006BK-0263"):
        ata_in[80] = 1.0

    if(request_data["type"]=="FW380009-019WH/HT"):
        ata_in[81] = 1.0

    if(request_data["type"]=="FW380009-032BL/HT"):
        ata_in[82] = 1.0

    if(request_data["type"]=="FW380009-032BL/HT/GR"):
        ata_in[83] = 1.0

    if(request_data["type"]=="FW380009-032WH/HT"):
        ata_in[84] = 1.0

    if(request_data["type"]=="FW380026-014"):
        ata_in[85] = 1.0

    if(request_data["type"]=="FW380026-014BK-0042"):
        ata_in[86] = 1.0

    if(request_data["type"]=="FW380026-014CR-0044"):
        ata_in[87] = 1.0

    if(request_data["type"]=="FW380026-014NI-0050"):
        ata_in[88] = 1.0

    if(request_data["type"]=="FW380026-014PP-0055"):
        ata_in[89] = 1.0

    if(request_data["type"]=="FW380026-014RW-0056"):
        ata_in[90] = 1.0

    if(request_data["type"]=="FW380026-014TA-0059"):
        ata_in[91] = 1.0

    if(request_data["type"]=="FW380026-014VA-0060"):
        ata_in[92] = 1.0

    if(request_data["type"]=="FW380026-014WH-0061"):
        ata_in[93] = 1.0

    if(request_data["type"]=="FW380034-015"):
        ata_in[94] = 1.0

    if(request_data["type"]=="FW380080-020BK-0148"):
        ata_in[95] = 1.0

    if(request_data["type"]=="FW380161-010"):
        ata_in[96] = 1.0

    if(request_data["type"]=="FW380230-025BK-1099"):
        ata_in[97] = 1.0

    if(request_data["type"]=="FW380471-032"):
        ata_in[98] = 1.0

   

    

    print(ata_in)
    print("----------------------------------------------------------------------------")



    x_in =np.array(ata_in).reshape(1,-1)
    # load model
    model = load_models()
    prediction = model.predict(x_in)[0]
    prediction=float(prediction)
    prediction2=0.0
    prediction3=0.0
    print(prediction)

    modeljac = load_modelsJac()
    predictionJac = modeljac.predict(x_in)[0]
    predictionJac=float(predictionJac)
    predictionJac2=0.0
    predictionJac3=0.0
    print(predictionJac)

    modelknt = load_modelsknt()
    predictionknt = modelknt.predict(x_in)[0]
    predictionknt=float(predictionknt)
    predictionknt2=0.0
    predictionknt3=0.0
    print(predictionknt)

    modelpk = load_modelspk()
    predictionpk = modelpk.predict(x_in)[0]
    predictionpk=float(predictionpk)
    predictionpk2=0.0
    predictionpk3=0.0
    print(predictionpk)

    modelqa = load_modelsqa()
    predictionqa = modelqa.predict(x_in)[0]
    predictionqa=float(predictionqa)
    predictionqa2=0.0
    predictionqa3=0.0
    print(predictionqa)

    modelwev = load_modelswev()
    predictionwev = modelwev.predict(x_in)[0]
    predictionwev=float(predictionwev)
    predictionwev2=0.0
    predictionwev3=0.0
    print(predictionwev)

    modelWP = load_modelsWP()
    predictionWP = modelWP.predict(x_in)[0]
    predictionWP=float(predictionWP)
    predictionWP2=0.0
    predictionWP3=0.0

    modeldye = load_modelsdye()
    predictiondye = modeldye.predict(x_in)[0]
    predictiondye=float(predictiondye)
    predictiondye2=0.0
    predictiondye3=0.0
    print(predictionWP)
    print("----------------------------------------------------------------------------")

    


    if(request_data["type"]=="FJ101980-032.0"):
        predictiondye="not a part of process"
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        

    if(request_data["type"]=="FJ103791-032.0"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        


    if(request_data["type"]=="FJ103880-032.0WH"):
        predictiondye="not a part of process"
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"
        

    if(request_data["type"]=="FK048204-008.5"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5BK-1142"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5BL-0857"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5BM-1441"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5BP-1373"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5CC-1385"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5CD-1340"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5FP-0820"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5LM-0923"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5MP-1400"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5MP-1408"):
        
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5PL-0926"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5SG-1407"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5SN-1383"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5WH-0834"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK048204-008.5WH-1039"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK054594-015"):
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK054595-008"):
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380002-007BK-0231"):
        predictionwev="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380002-007BK-1200"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008(15G)"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008BK-0042"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008BS-0043"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008CR-0044"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008GA-0046"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008MK-0277"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008NI-0050"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008PL-0054"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008PP-0055"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008RW-0056"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008SD-0057"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008SP-0058"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008TA-0059"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380028-008WH-0061"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380038-011BK"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380038-011BK/GR"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380038-011SD"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380051-056BK/CT"):
        predictionwev="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380051-058BK/CT"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380051-058SD/CT"):
         predictionwev="not a part of process"
         predictionJac="not a part of process"

    if(request_data["type"]=="FK380052-008"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380052-008WH-0070"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380075-025SD"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380078-08.5BK-0250"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380087-032BK"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380087-032SD/CT"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380111-006BK/CT"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380111-006SD/CT"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380112-006SD"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380120-022BK/CT"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380120-022SD/CT"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380120-029BK/CT"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380120-029SD/CT"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380120-029SD/CT/GR"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380120-083SD/GR"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380122-025SD"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380212-010"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380212-010WH-0834"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380239-003SD"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380334-010.5"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380334-010.5SG-1061"):
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380334-010.5WH-1041"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380504-008BK"):
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380504-008SD"):
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380617-004WH-1704"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FK380642-012BK"):
        predictiondye="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW002007-004"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW002007-004BK-1092"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW002007-004MG-1093"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW002007-004WH-1095"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW002007-006BK-1092"):
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW002007-006MG-1093"):
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW002007-006WH-1095"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW051849-007.5"):
        predictionknt="not a part of process"
        predictiondye="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW101426-017.0"):
        predictionknt="not a part of process"
        predictiondye="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380006-006BK-0263"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380009-019WH/HT"):
        predictionknt="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380009-032BL/HT"):
        predictionknt="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380009-032BL/HT/GR"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380009-032WH/HT"):
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380026-014"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380026-014BK-0042"):
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380026-014CR-0044"):
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380026-014NI-0050"):
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380026-014PP-0055"):
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380026-014RW-0056"):
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380026-014TA-0059"):
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380026-014VA-0060"):
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380026-014WH-0061"):
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380034-015"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380080-020BK-0148"):
        predictionknt="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380161-010"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380230-025BK-1099"):
        predictionknt="not a part of process"
        predictionwev="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"

    if(request_data["type"]=="FW380471-032"):
        predictionpk="not a part of process"
        predictionqa="not a part of process"
        predictiondye="not a part of process"
        predictionknt="not a part of process"
        predictionWP="not a part of process"
        predictionJac="not a part of process"
    tot=0.0

    if(predictionWP!="not a part of process"):
        tot=tot+predictionWP
   

    if(predictiondye!="not a part of process"):
        tot=tot+predictiondye
   

    if(predictionJac!="not a part of process"):
        tot=tot+predictionJac
   

    if(predictionknt!="not a part of process"):
        tot=tot+predictionknt
    

    if(predictionpk!="not a part of process"):
        tot=tot+predictionpk
    

    if(predictionwev!="not a part of process"):
        tot=tot+predictionwev
    

    if(predictionqa!="not a part of process"):
        tot=tot+predictionqa

    print(tot)
    
    if(tot!=0.0):
        if(predictionWP=="not a part of process"):
            predictionWP1=predictionWP
        else:
            predictionWP=predictionWP/tot*prediction
            predictionWP2=predictionWP
            predictionWP1=predictionWP/100.0*q
            predictionWP3=predictionWP1
        if(predictiondye=="not a part of process"):
            predictiondye1=predictiondye
        else:
            predictiondye=predictiondye/tot*prediction
            predictiondye2=predictiondye
            predictiondye1=predictiondye/100.0*q
            predictiondye3=predictiondye1
        if(predictionJac=="not a part of process"):
                predictionJac1=predictionJac
        else:
            predictionJac=predictionJac/tot*prediction
            predictionJac2=predictionJac
            predictionJac1=predictionJac/100.0*q
            predictionJac3=predictionJac1
        if(predictionknt=="not a part of process"):
            predictionknt1=predictionknt
        else:
            predictionknt=predictionknt/tot*prediction
            predictionknt2=predictionknt
            predictionknt1=predictionknt/100.0*q
            predictionknt3=predictionknt1
        if(predictionpk=="not a part of process"):
             predictionpk1=predictionpk
        else:
            predictionpk=predictionpk/tot*prediction
            predictionpk2=predictionpk
            predictionpk1=predictionpk/100.0*q
            predictionpk3=predictionpk1
        if(predictionwev=="not a part of process"):
            predictionwev1=predictionwev
        else:
            predictionwev=predictionwev/tot*prediction
            predictionwev2=predictionwev
            predictionwev1=predictionwev/100.0*q
            predictionwev3=predictionwev1
        if(predictionqa=="not a part of process"):
            predictionqa1=predictionqa
        else:
            predictionqa=predictionqa/tot*prediction
            predictionqa2=predictionqa
            predictionqa1=predictionqa/100.0*q
            predictionqa3=predictionqa1
    else:
        if(predictionWP=="not a part of process"):
            predictionWP1=predictionWP
        else:
            predictionWP=0.0
            predictionWP2=predictionWP
            predictionWP1=0.0
            predictionWP3=predictionWP1
        if(predictiondye=="not a part of process"):
            predictiondye1=predictiondye
        else:
            predictiondye=0.0
            predictiondye2=predictiondye
            predictiondye1=0.0
            predictiondye3=predictiondye1
        if(predictionJac=="not a part of process"):
                predictionJac1=predictionJac
        else:
            predictionJac=0.0
            predictionJac2=predictionJac
            predictionJac1=0.0
            predictionJac3=predictionJac1
        if(predictionknt=="not a part of process"):
            predictionknt1=predictionknt
        else:
            predictionknt=0.0
            predictionknt2=predictionknt
            predictionknt1=predictionknt/100.0*q
            predictionknt3=0.0
        if(predictionpk=="not a part of process"):
             predictionpk1=predictionpk
        else:
            predictionpk=0.0
            predictionpk2=predictionpk
            predictionpk1=0.0
            predictionpk3=predictionpk1
        if(predictionwev=="not a part of process"):
            predictionwev1=predictionwev
        else:
            predictionwev=0.0
            predictionwev2=predictionwev
            predictionwev1=0.0
            predictionwev3=predictionwev1
        if(predictionqa=="not a part of process"):
            predictionqa1=predictionqa
        else:
            predictionqa=0.0
            predictionqa2=predictionqa
            predictionqa1=0.0
            predictionqa3=predictionqa1
        

        

    

   

    
    

   

    # response = json.dumps({'response': prediction})
    response = json.dumps({
    "response": prediction,
    "jac":predictionJac,
    "knt":predictionknt,
    "pk":predictionpk,
    "wev":predictionwev,
    "WP":predictionWP,
    "qa":predictionqa, 
    "dye":predictiondye,
    "q":q,
    "jac1":predictionJac1,
    "knt1":predictionknt1,
    "pk1":predictionpk1,
    "wev1":predictionwev1,
    "WP1":predictionWP1,
    "qa1":predictionqa1, 
    "dye1":predictiondye1,
    "responsed": prediction2,
    "jacd":predictionJac2,
    "kntd":predictionknt2,
    "pkd":predictionpk2,
    "wevd":predictionwev2,
    "WPd":predictionWP2,
    "qad":predictionqa2, 
    "dyed":predictiondye2,
    "qd":q,
    "jac1d":predictionJac3,
    "knt1d":predictionknt3,
    "pk1d":predictionpk3,
    "wev1d":predictionwev3,
    "WP1d":predictionWP3,
    "qa1d":predictionqa3, 
    "dye1d":predictiondye3,

    })
    print(response)





    return response



 
if __name__ == '__main__':
    app.debug = True
    app.run()