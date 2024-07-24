from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json

with open('config.json', 'r') as c:
    param = json.load(c)["param"]

local_server = True
app = Flask(__name__)
mail= Mail(app)
if(local_server):
        app.config["SQLALCHEMY_DATABASE_URI"] = param['local_uri']
else:
       app.config["SQLALCHEMY_DATABASE_URI"] = param['prod_uri']
       
db = SQLAlchemy(app)


class Contact(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(20), nullable=False)
    

@app.route("/")
def home():
        return render_template("index.html", param=param)

@app.route("/about")
def about():
        name="avinash"
        return render_template('about.html', param=param)

@app.route("/contact", methods=['GET','POST'])
def contact(): 
        if(request.method=='POST'):
                name=request.form.get('name')
                email=request.form.get('email')
                phone=request.form.get('phone')
                message=request.form.get('message')
                entry=Contact(name=name,email=email,phone_num=phone,message=message)
                db.session.add(entry)
                db.session.commit()
        return render_template('contact.html', param=param)

app.run(debug=True) 