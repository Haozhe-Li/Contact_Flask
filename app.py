from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER'] = str(os.getenv('MAIL_SERVER'))
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = str(os.getenv('MAIL_USERNAME'))
app.config['MAIL_PASSWORD'] = str(os.getenv('MAIL_PASSWORD'))

SENDER = str(os.getenv('MAIL_SENDER'))
FORWARD = str(os.getenv('MAIL_FORWARD'))
NAME = str(os.getenv('MAIL_NAME'))

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
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
    to_client_msg.body = f"[Auto-Reply] Thank you for contacting me! I will get back to you soon. \n\n Sincerely, \n {NAME}"
    try:
        mail.send(to_client_msg)
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'send to client failed'}), 500
    try:
        mail.send(to_myself_msg)
        return jsonify({'message': 'Email sent!'}), 200
    except Exception as e:
        return jsonify({'error': str(e), 'message':'forward to myself failed'}), 500

@app.route('/')
def index():
    return 'Hi! This is a simple email server, and welcome to my project!'

if __name__ == '__main__':
    app.run(debug=True)
