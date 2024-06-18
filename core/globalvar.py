import time
import os

SENDER = str(
    os.getenv("MAIL_SENDER")
)  # your email address, could be the same as MAIL_USERNAME
FORWARD = str(
    os.getenv("MAIL_FORWARD")
)  # the email address you want to forward the contact form to
NAME = str(os.getenv("MAIL_NAME"))  # your name
SOURCE = str(
    os.getenv("VALID_REQUEST_SOURCE")
)  # the source of the request, e.g. your website
DATE = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
