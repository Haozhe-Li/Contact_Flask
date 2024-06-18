from core.globalvar import *
from flask import Flask, request, jsonify


def is_request_from_my_website():
    if SOURCE == "False":
        return True  # bypass
    referer = request.headers.get("Referer")
    return SOURCE in referer if referer else False
