from flask import Flask, request, render_template
from flask.templating import render_template
from flask_mail import Message, Mail
from itsdangerous import URLSafeTimedSerializer
from random import *

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
mail = Mail(app)
otp = randint(00000, 99999)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=["POST"])
def verify():
    email = request.form['email']
    msg = Message(subject="OTP", sender='hayknikogosyan60@gmail.com', recipient=[email])
    msg.body=str(otp)
    mail.send(msg)
    return render_template('verify.html')

@app.route('/validate', methods=["POST"])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return "Success"
    return "try again"

if __name__ == "__main__":
    app.run(debug=True)