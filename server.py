# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///hotel.db"
# 
# db=SQLAlchemy(app)
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# if __name__=="__main__":
#     app.run(debug=True)


import json



from re import S
from flask import Flask, request, jsonify
import flask_login
from flask_sqlalchemy import SQLAlchemy 

from flask_login import LoginManager, UserMixin,login_required,login_user,logout_user

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''@localhost/users'
# DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='dikshadaryani99', server='localhost', database='users')
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:dikshadaryani99@localhost/users"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config['SECRET_KEY'] = 'secretKey'
app.config['TESTING']=False

db = SQLAlchemy(app)
login_manager=LoginManager()
login_manager.init_app(app)



"""Table for storing the users"""

class user(db.Model,UserMixin):
    # id = db.Column(db.Integer, primary_key = True)
    __tablename__='user'
    # id=db.Column(db.Integer,unique = True,autoincrement=True)
    username = db.Column(db.String(100),primary_key = True,unique = True)
    password = db.Column(db.String(100))
    loginornot=db.Column(db.Integer,default=0)
 
 
    def __init__(self, username, password,loginornot):
        self.username = username
        self.password = password
        self.loginornot=loginornot
        
    def get_id(self):
        print("Get id called")
        # print(self.id)
        return self.username




"""Table for storing the menu """


class menu(db.Model,UserMixin):
    # id = db.Column(db.Integer, primary_key = True)
    __tablename__='menu'
    itemno = db.Column(db.Integer,primary_key = True,unique = True)
    halfprice = db.Column(db.Integer,nullable=False)
    fullprice = db.Column(db.Integer,nullable =False)
 
    def __init__(self, itemno, halfprice,fullprice):
        self.itemno = itemno
        self.halfprice = halfprice
        self.fullprice=fullprice
    # def get_id(self):
    #     return self.username



"""table for storing the orders"""

class foodorder(db.Model,UserMixin):
    # id = db.Column(db.Integer, primary_key = True)
    __tablename__='foodorder'
    orderid = db.Column(db.Integer,primary_key = True,unique = True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    # itemno = db.Column(db.Integer,nullable =False)
    orderdetails= db.Column(db.String(100),nullable=False)
    totalprice= db.Column(db.Integer,nullable =False)
 
    def __init__(self, username,orderdetails,totalprice):
        
        self.username=username

        self.orderdetails= orderdetails
        self.totalprice = totalprice
        
"""Table for storing the bills"""



class bill(db.Model,UserMixin):
    # id = db.Column(db.Integer, primary_key = True)
    __tablename__='bill'
    billid = db.Column(db.Integer,primary_key = True,unique = True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    # itemno = db.Column(db.Integer,nullable =False)
    discount_increase= db.Column(db.String(100),nullable=False)
    tip= db.Column(db.Integer,nullable=False)
    finaltotal= db.Column(db.Integer,nullable =False)
 
    def __init__(self,username,discount_increase, tip,finaltotal):
        
        self.username=username

        self.discount_increase = discount_increase
        self.tip =tip
        self.finaltotal=finaltotal
# def job():
#     data = menu.query.all()
#     print(data)

    
@login_manager.user_loader
def load_user (user_id):
    print("hi inside the userloader")
    print(user_id)
    return user.query.get(user_id)
    
# @app.before_first_request(job())




"""Route for signup"""

@app.route('/signup', methods = [ 'POST'])
def signup():
    
    posted = request.get_json()
    username = posted['username']
    print(username)
    password = posted['password']
    loginornot=0
    print(password)
    check_user = user.query.filter_by(username = username).first()
    if check_user:
        return "User already exists."
    new_user = user(username=username,password=password,loginornot=loginornot)
    db.session.add(new_user)
    db.session.commit()
    return "User added sucessfully."

# @app.route('/read')
# def read():
#     data = Student.query.all()
#     resp = {}
#     if len(data) == 0:
#             respo = {
#                 "response": "No Entries have been added yet"
#             }
#             return respo
    
#     for i in data:
#         resp[i.id] = {'name':i.name, 'stream': i.stream}
#     return jsonify(resp)



"""Route for signing in """


@app.route('/signin', methods = ['POST'])
def signin():
  
    posted = request.get_json()
   
    username = posted['username']
    print(username)
    password = posted['password']
    print(password)
    check_user = user.query.filter_by(username=username).first()
    if check_user:
        if check_user.password==password:
            login_user(check_user)

            if(check_user.loginornot==1):
                return "You are already logged in"
            else:
                check_user.loginornot=1
                
                
                db.session.commit()
                return "LOG IN SUCCESSFUL"
        else:
            return "wrong password"
    else:
        return "no such user"


"""Route for logout"""

@app.route('/signout',methods=['POST','GET'])
# @login_required
def signout():
    if(request.method=="POST"):
        posted = request.get_json()
        # print("in the post ")
        username = posted['username']
        # print(username)
        # uname=username
        # print(uname)
        # return "username sent"
        check_user = user.query.filter_by(username=username).first()
        if check_user.loginornot==1:
            # logout_user()
            check_user.loginornot=0
            db.session.commit()
            return "log out successful"
        else:
            return "You have not logged in"
            

"""Route for reading the menu"""


@app.route('/read',methods=['GET'])
def read():
    data = menu.query.all()
    resp = {}
    if len(data) == 0:
            respo = {
                "response": "No Entries have been added yet"
            }
            return respo
    print(data)
    for i in data:
        resp[i.itemno] = {'halfprice':i.halfprice, 'fullprice': i.fullprice}
    return jsonify(resp)

uname=""
@app.route('/readbill' , methods = ['POST','GET'])

def readbill():
    global uname
    print("hello")
    
    print("the curent user is")
    if(request.method=="POST"):
        posted = request.get_json()
        print("in the post ")
        username = posted['username']
        print(username)
        uname=username
        print(uname)
        return "username sent"
    # print(flask_login.current_user)
    if request.method=="GET":
        print("in the get ")
        str=uname
        print(uname)
        data = bill.query.filter_by(username=uname).all()
        print(data)
        resp = {}
        
        # if len(data) == 0:
        #         respo = {
        #             "response": "No Entries have been added yet"
        #         }
        #         return respo
        finallist=[]
        print("hello")
        print(data)
        for i in data:
            print("hello")
            print(i)
            finalresp=(foodorder.query.filter_by(orderid=i.billid).all())
            print(finalresp)
            for each in finalresp:
                resp[each.orderid] = {'orderid':i.billid, 'orderdetails': each.orderdetails,'totalprice': each.totalprice, 'discount_increase': i.discount_increase,
                'tip':i.tip, 'finaltotal':i.finaltotal}
        print(type(resp))
        print(resp)
        # print(json.loads(jsonify(resp).content)) 
        return resp




"""Route for adding items into the database"""


@app.route('/additems', methods = [ 'POST'])
def additems():
    print("koko")
    posted = request.get_json()
    itemno = posted['itemno']
    print(itemno)
    halfprice = posted['halfprice']
    print(halfprice)
    fullprice = posted['fullprice']
    print(fullprice)
    check_item = menu.query.filter_by(itemno = itemno).first()
    if check_item:
        return "item already exists."
    new_item = menu(itemno=itemno,halfprice=halfprice,fullprice=fullprice)
    db.session.add(new_item)
    db.session.commit()
    return "item added sucessfully."


"""Route forr ordering items"""



@app.route('/orderitems', methods = [ 'POST'])
def orderitems():
    # print("koko")
    posted = request.get_json()
    # orderid = posted['orderid']
    # itemno = posted['itemno']
    # print(itemno)
    username = posted['username']
    print(username)
    items = posted['orderdetails']
    print(items)
    total = posted['totalprice']
    # check_order = foodorder.query.filter_by(orderid = orderid).first()
    # if check_order:
        # return "Order already exists."

#     for each in l:
#     str+="%".join(each)
#     str+="%"
# str=str[:len(str)-1]
# print(str)
    str=""
    for each in items:
        str+="&".join(each)
        str+="&"

    str=str[:len(str)-1]
    print(str)
    new_order = foodorder(username=username,orderdetails=str,totalprice=total)
    db.session.add(new_order)
    db.session.commit()
    return "order added sucessfully."



"""Route for adding bill"""

@app.route('/addbill', methods = [ 'POST'])
def addbill():
    # print("koko")
    posted = request.get_json()
    # orderid = posted['orderid']
    # itemno = posted['itemno']
    # print(itemno)
    username = posted['username']
    print(username)
    discount_increase = posted['discount_increase']
    print(discount_increase)
    tip = posted['tip']
    finaltotal = posted['finaltotal']
    # print(discount_increase)
    # check_order = foodorder.query.filter_by(orderid = orderid).first()
    # if check_order:
        # return "Order already exists."
    # str=""
    # for each in items:
    #     str="&".join(each)
    #     str+="&"

    # str=str[:len(str)-1]
# print(str)
    new_bill = bill(username=username,discount_increase=discount_increase,tip=tip,finaltotal=finaltotal)
    db.session.add(new_bill)
    db.session.commit()
    return "bill added sucessfully."


"""Entry program"""

if __name__ == '__main__':
    # db.create_all()
    print("hello")
    # data = menu.query.all()
    # print(data)
    for row in user.query:
        row.loginornot=0
    db.session.commit()
    app.run(port=5000, debug=True)