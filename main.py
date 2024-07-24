from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json

# Load configuration from config.json
with open('config.json', 'r') as c:
    param = json.load(c)["param"]

# Determine if running on local server
local_server = True

app = Flask(__name__)
mail = Mail(app)

# Configure SQLAlchemy database URI
if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = param['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = param['prod_uri']

db = SQLAlchemy(app)

# Define Contact model
class Contact(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(20), nullable=False)

# Home route
@app.route("/")
def home():
    return render_template("index.html", param=param)

# About route
@app.route("/about")
def about():
    return render_template('about.html', param=param)

# Contact route
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, email=email, phone_num=phone, message=message)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html', param=param)

# Run the app on host 0.0.0.0 and a specified port (e.g., 5000)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
