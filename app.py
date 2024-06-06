# THIS IS A DEMO HTML FOR CONTACT FLASK PROJECT
# AUTHOR: HAOZHE LI
# DATE: JUNE 6 2024
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import time

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER'] = str(os.getenv('MAIL_SERVER')) # your SMTP email server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = str(os.getenv('MAIL_USERNAME')) # your email username (don't use alias email name, use the real email name)
app.config['MAIL_PASSWORD'] = str(os.getenv('MAIL_PASSWORD')) # your email password, you probably need to generate a secret key or app-specific password

SENDER = str(os.getenv('MAIL_SENDER')) # your email address, could be the same as MAIL_USERNAME
FORWARD = str(os.getenv('MAIL_FORWARD')) # the email address you want to forward the contact form to
NAME = str(os.getenv('MAIL_NAME')) # your name
SOURCE = str(os.getenv('VALID_REQUEST_SOURCE')) # the source of the request, e.g. your website
DATE = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

mail = Mail(app)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute", "60 per hour"] # limit the number of requests to 10 per minute and 60 per hour
)

def is_request_from_my_website():
    if SOURCE =='False':
        return True # bypass
    referer = request.headers.get('Referer')
    return SOURCE in referer if referer else False

@app.route('/send_email', methods=['POST'])
@limiter.limit("5 per minute") # limit the number of requests to 10 per minute
def send_email():
    if not is_request_from_my_website():
        return jsonify({'message': 'Invalid request source'}), 403
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    to_myself_msg = Message('New Contact Form Submission',
                  sender=SENDER,
                  recipients=[FORWARD])
    to_myself_msg.body = f"""
    From: {name} <{email}>
    Message:
    {message}
    """
    to_client_msg = Message('[Auto-Reply] Thank you for contacting me!',
                  sender=SENDER,
                  recipients=[email])
    to_client_msg.body = f"[Auto-Reply] Thank you for contacting me! I will get back to you soon. \n\n Sincerely, \n {NAME}, {DATE}"
    try:
        mail.send(to_client_msg)
    except Exception as e:
        return jsonify({'message': 'send to client failed. Service halt.'}), 500
    try:
        mail.send(to_myself_msg)
        return jsonify({'message': 'Email sent!'}), 200
    except Exception as e:
        return jsonify({'message':'forward to myself failed'}), 500

@app.route('/')
def index():
    return 'Hi! This is a simple email server, and welcome to my project!'

if __name__ == '__main__':
    app.run(debug=True)
