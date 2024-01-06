import mysql.connector
import json
from flask import make_response
from datetime import datetime,timedelta
import jwt
class user_model():
    def __init__(self):
        #used to establish connection
        try:
            self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="flask_learn")
            self.conn.autocommit=True
            #for read operation cursor is used
            self.cur=self.conn.cursor(dictionary=True)
            print('connection successful')
        except:
            print('connection unsuccessful')
    
    '''used to return value to database
    def user_getall_model(self):
        return "this is user getall model"'''

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        if len(result)>0:
            #return json string
            #return json.dumps(result)

            #returns json 
            #return result

            #return {"payload":result}

            #sending response object
            #return make_response({"payload":result},200)
        
            #return along with header
            res=make_response({"payload":result},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            #return "No Data"
            return make_response({"message":"No data"},204)
        
    def user_addone_model(self,data):
        #self.cur.execute("SELECT * FROM users")
        #using POSTMAN API to add into MYSQL database
        self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        #print(data)
        #return "user added successfully"
        #return {"message":"user added successfully"}
        return make_response({"message":"user added successfully"},200)
    
    def user_update_model(self,data):
        #using POSTMAN API to update in MYSQL database
        self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return "user updated successfully"
        else:
            return "no rows to update"
        
    def user_delete_model(self,id):
        #using POSTMAN API to update in MYSQL database
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return "user deleted successfully"
        else:
            return "no rows to delete"
        
    def user_patch_model(self,data,id):
        qry="UPDATE users SET "
        for key in data:
            qry+= f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id={id}"
        self.cur.execute(qry)

        if self.cur.rowcount>0:
            return make_response({"message":"User updated successfully"},201)
        else:
            return make_response({"message":"Nothing to update"},202)
        
    def user_pagination_model(self,limit,page):
        limit=int(limit)
        page=int(page)
        start=(page*limit)-limit

        qry=f"SELECT * FROM users LIMIT {start}, {limit}"
        self.cur.execute(qry)

        result=self.cur.fetchall()
        if len(result)>0:
            res=make_response({"payload":result,"page":page,"limit":limit},200)
            return res
        else:
            #return "No Data"
            return make_response({"message":"No data"},204)
        
    def user_upload_avatar_model(self,uid,filePath):
        self.cur.execute(f"UPDATE users SET avatar='{filePath}' WHERE id={uid}")
        if self.cur.rowcount>0:
            return make_response({"message":"file uploaded successfully"},201)
        else:
            return make_response({"message":"nothing to update"},202)
    
    def user_login_model(self,data):
        self.cur.execute(f"SELECT id,name,email,phone,avatar,role_id FROM users WHERE email='{data['email']}' and password='{data['password']}'")
        result=self.cur.fetchall()
        userdata=result[0]
        exp_time=datetime.now()+timedelta(minutes=15)
        #to convert to epoch format use timestamp()
        exp_epoch_time=int(exp_time.timestamp())
        payload={
            "payload":userdata,
            "exp":exp_epoch_time
        }
        jwtoken=jwt.encode(payload,"meena",algorithm="HS256")
        return make_response({"token":jwtoken},200)














                  
