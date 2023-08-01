from flask import Flask,request,jsonify

app=Flask(__name__)#here we are creating an object for Flask

@app.route('/abc',methods=['GET','POST'])#route is a function available in flask
#calling object app and giving route for function below as /abc through get,post operations
# '@' means after this line call all functions
#get means getting data in url(in url iteslf ur given data visible like google search we cn see
#post means as a part of body we will send like username and password not visible in any url like gmail

def test1():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a+b
        return jsonify((str(result)))

@app.route('/abc1/sus',methods=['GET','POST'])#api we are calling route by url not function name so any sever with diff language can undertand
def test2():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify((str(result)))

@app.route('/abc1/sus/test',methods=['GET','POST'])#api we are calling route by url not function name so any sever with diff language can undertand
def test3():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a ** b
        return jsonify((str(result)))

@app.route('/abc1/sus/test4',methods=['GET','POST'])#api we are calling route by url not function name so any sever with diff language can undertand
def test4():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a - b
        return jsonify((str(result)))

@app.route('/abc1/sus/test5',methods=['GET','POST'])#api we are calling route by url not function name so any sever with diff language can undertand
def test5():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a / b
        return jsonify((str(result)))



if __name__=='__main__':#to invoke entire python main classess
    app.run()


#1 . Write a program to insert a record in sql table via api
#2.  Write a program to update a record via api
#3 . Write a program to delete a record via api
#4 . Write a program to fetch a record via api
#5 . All the above questions you have to answer for mongo db as well .

