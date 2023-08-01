from flask import Flask,request,jsonify
import mysql.connector as conn

mydb=conn.connect(host="localhost",user="root",passwd="Susmitha")
print(mydb)

app=Flask(__name__)


@app.route('/create',methods=['GET','POST'])
def Create():
    if(request.method=='POST'):
        _json=request.json
        _employee_id = _json['employee_id']
        _emp_name=_json['emp_name']
        _emp_mailid=_json['emp_mailid']
        _emp_salary=_json['emp_salary']
        _emp_attendance=_json['emp_attendance']
        sql="insert into susmitha.susdetails(employee_id,emp_name,emp_mailid,emp_salary,emp_attendance)Values(%s,%s,%s,%s,%s)"
        data=(_employee_id,_emp_name,_emp_mailid,_emp_salary,_emp_attendance)
        cursor=mydb.cursor()
        cursor.execute(sql,data)
        mydb.commit()

        resp = jsonify('User added successfully!')
        return resp

@app.route('/update',methods=['GET','POST'])
def Update():
    if(request.method=='POST'):
        _json = request.json

        _employee_id = _json['employee_id']
        _emp_name = _json['emp_name']
        _emp_mailid = _json['emp_mailid']
        _emp_salary = _json['emp_salary']
        _emp_attendance = _json['emp_attendance']
        sql="UPDATE susmitha.susdetails SET emp_salary=emp_salary+50000 WHERE emp_attendance=50"
        data=(_employee_id,_emp_name,_emp_mailid,_emp_salary,_emp_attendance)
        cursor=mydb.cursor()
        cursor.execute(sql)
        mydb.commit()

        resp = jsonify('User updated successfully!')
        return resp

@app.route('/delete',methods=['GET','POST'])
def Delete():
    if(request.method=='POST'):
        _json = request.json
        _employee_id = _json['employee_id']
        _emp_name = _json['emp_name']
        _emp_mailid = _json['emp_mailid']
        _emp_salary = _json['emp_salary']
        _emp_attendance = _json['emp_attendance']
        sql="DELETE from susmitha.susdetails  WHERE emp_attendance=30;"
        data=(_employee_id,_emp_name,_emp_mailid,_emp_salary,_emp_attendance)
        cursor=mydb.cursor()
        cursor.execute(sql)
        mydb.commit()

        resp = jsonify('Deleted user successfully!')
        return resp

@app.route('/fetchall',methods=['GET','POST'])
def Fetchall():
    if(request.method=='POST'):
        cursor = mydb.cursor()
        sql="select * from susmitha.susdetails"
        #data=(_employee_id,_emp_name,_emp_mailid,_emp_salary,_emp_attendance)
        cursor.execute(sql)
        r=[]
        for resp in cursor.fetchall():
            r.append(resp)

        return jsonify(r)

        mydb.commit()

if __name__=='__main__':
    app.run()


