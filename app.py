from flask import Flask, render_template
import requests
import os
import pwd
import tzlocal


app = Flask(__name__)

@app.route("/")
def hello():
    with open("/etc/hostname", "r") as f:
        container_id = f.read().strip()
    container_username = pwd.getpwuid(os.getuid()).pw_name
    availability_zone = 'UTC'
    meta = {
        'container_id': container_id,
        'container_username': container_username,
        'availability_zone': availability_zone
    }

    return render_template("index.html", meta=meta)