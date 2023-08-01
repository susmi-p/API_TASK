from flask import Flask,request,jsonify
import pymongo


client=pymongo.MongoClient("mongodb+srv://susmitha:susmitha@cluster0.ox0skuv.mongodb.net/?retryWrites=true&w=majority")
db=client.test

app=Flask(__name__)

@app.route('/create',methods=['GET','POST'])
def Create():
    if(request.method=='POST'):
        _json=request.json
        list_of_records=request.json
        _companyName = _json['companyName']
        _product = _json['product']
        _courseOffered= _json['courseOffered']

        database = client['myinfo']
        collection = database['sus']
        collection.insert_many([list_of_records])
        resp = jsonify('User added successfully!')
        return resp

@app.route('/update',methods=['GET','POST'])
def Update():
    if(request.method=='POST'):
        _json=request.json
        list_of_records=request.json
        _companyName = _json['companyName']
        _product = _json['product']
        _courseOffered= _json['courseOffered']

        database = client['myinfo']
        collection = database['sus']

        data={'companyName':'skybags'}
        updata={"$set":{"companyName":'HP'}}

        collection.update_one(data,updata)
        for x in collection.find():
            print(x)
        resp = jsonify('User updated successfully!')
        return resp

@app.route('/delete',methods=['GET','POST'])
def Delete():
    if(request.method=='POST'):
        _json=request.json
        database = client['myinfo']
        collection = database['sus']

        deldata={"product":"Affordable AI"}

        collection.delete_one(deldata)
        for x in collection.find():
            print(x)
        resp = jsonify('User deleted successfully!')
        return resp


@app.route('/fetch', methods=['GET', 'POST'])
def Fetch():
    if (request.method == 'POST'):

        database = client['myinfo']
        collection = database['sus']

        x=collection.find()
        resp=[]
        for r in x:
            r['_id']=str(r['_id'])
            resp.append(r)
        print(resp)

        return jsonify(resp)


if __name__=='__main__':
    app.run()
