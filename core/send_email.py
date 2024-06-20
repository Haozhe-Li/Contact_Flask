from flask import Flask, request, jsonify
from flask_mail import Mail, Message

from core.globalvar import *
from core.utils import *


def send_message(data, mail):
    name = data.get("name")
    if name == "test":
        return jsonify({"message": "Endpoint is working! Test success."}), 200
    email = data.get("email")
    message = data.get("message")
    to_myself_msg = Message(
        "New Contact Form Submission", sender=SENDER, recipients=[FORWARD]
    )
    to_myself_msg.body = f"""
    From: {name} <{email}>
    Message:
    {message}
    """
    to_client_msg = Message(
        "[Auto-Reply] Thank you for contacting me!", sender=SENDER, recipients=[email]
    )
    to_client_msg.body = f"[Auto-Reply] Thank you for contacting me! I will get back to you soon. \n\n Sincerely, \n {NAME}, {DATE}"
    try:
        mail.send(to_client_msg)
    except Exception as e:
        return jsonify({"message": "send to client failed. Service halt."}), 500
    try:
        mail.send(to_myself_msg)
        return jsonify({"message": "Email sent!"}), 200
    except Exception as e:
        return jsonify({"message": "forward to myself failed"}), 500
