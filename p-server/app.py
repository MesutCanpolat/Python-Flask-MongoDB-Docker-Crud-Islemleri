from flask import Flask,request,jsonify
import pymongo
from bson.objectid import ObjectId
myclient = pymongo.MongoClient("mongodb://root:example@mongo:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["ogrenci"]
app = Flask(__name__)


@app.route('/', methods=['POST'])
def add_ogrenci():
    x = mycol.insert_one(request.json)
    return "Başarılı"
@app.route('/', methods=['GET'])
def get_ogrenciler():
    showDataList = []
    for i in mycol.find({}):
        i['_id'] = str(i['_id']) 
        showDataList.append(i)
    return jsonify(showDataList)
@app.route('/<string:id>', methods=['GET'])
def get_ogrenci(id):
    ogrenci=mycol.find_one({"_id": ObjectId(id)})
    if(ogrenci is not None):
        ogrenci['_id'] = str(ogrenci['_id']) 
    return jsonify(ogrenci)
@app.route('/<string:id>', methods=['DELETE'])
def delete_ogrenci(id):
    mycol.delete_one({"_id": ObjectId(id)})
    return "Başarılı"
@app.route('/<string:id>', methods=['PUT'])
def update_ogrenci(id):
    mycol.update_one({"_id": ObjectId(id)},{ "$set": request.json })
    return "Başarılı"