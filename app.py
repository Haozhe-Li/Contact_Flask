# THIS IS A DEMO HTML FOR CONTACT FLASK PROJECT
# AUTHOR: HAOZHE LI
# DATE: JUNE 6 2024
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

from core.globalvar import *
from core.utils import *
from core.send_email import send_email


app = Flask(__name__)
CORS(app)
mail = Mail(app)

app.config["MAIL_SERVER"] = str(os.getenv("MAIL_SERVER"))  # your SMTP email server
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = str(
    os.getenv("MAIL_USERNAME")
)  # your email username (don't use alias email name, use the real email name)
app.config["MAIL_PASSWORD"] = str(
    os.getenv("MAIL_PASSWORD")
)  # your email password, you probably need to generate a secret key or app-specific password

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[
        "10 per minute",
        "60 per hour",
    ],  # limit the number of requests to 10 per minute and 60 per hour
)


@app.route("/send_email", methods=["POST"])
@limiter.limit("5 per minute")  # limit the number of requests to 10 per minute
def send_email():
    if not is_request_from_my_website():
        return jsonify({"message": "Invalid request source"}), 403
    data = request.json
    return send_email(data, mail)


@app.route("/")
def index():
    return "Hi! This is a simple email server, and welcome to my project!"


if __name__ == "__main__":
    app.run(debug=True)
