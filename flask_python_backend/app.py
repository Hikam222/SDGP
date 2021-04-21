from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
title = "sample application with Flask and MongoDB"
heading = "Elastic"

client = MongoClient("mongodb://Thamadie:test@test-shard-00-00.an6bk.mongodb.net:27017,test-shard-00-01.an6bk.mongodb.net:27017,test-shard-00-02.an6bk.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-xhe6nj-shard-0&authSource=admin&retryWrites=true&w=majority") #host uri
db = client.elasticdatabase    #Select the database
CORS(app)

@app.route('/')
def index():
    return render_template('home.html')

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

@app.route('/search', methods=['GET'])
def search(refer):
	#Searching a Data with various references
        key=request.values.get("key")
        refer=request.values.get("refer")
        if(key=="_id"):
            print("**************************")
            allData = db['elastic'].find({refer:ObjectId(key)})
        
        else:
            allData = db['elastic'].find({refer:key})
            print(refer)
            print(key)
            dataJson1 = []
            for search in allData:
                id = search['_id']
                JobNo = search['JobNo']
                ItemCode = search['ItemCode']
                ColorGroup = search['ColorGroup']
                Total_Quantity = search['Total_Quantity']
                Total_Wastage = search['Total_Wastage']
                waste_pecentage = search['waste_pecentage']

                dataDict = {
                    'id': str(id),
                    'JobNo': JobNo,
                    'ItemCode': ItemCode,
                    'ColorGroup': ColorGroup,
                    'Total_Quantity': Total_Quantity,
                    'Total_Wastage': Total_Wastage,
                    'waste_pecentage': waste_pecentage

                }
            
        dataJson1.append(dataDict)
        # print(dataJson)
        return jsonify(dataJson1)

if __name__ == '__main__':
    app.debug = True
    app.run()