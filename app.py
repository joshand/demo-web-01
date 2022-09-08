from flask import Flask, stream_template
import random
import string
import os


app = Flask(__name__)
image_server_ip_address = os.environ.get('IMG_SVR_IP', "127.0.0.1")
image_server_prt_number = os.environ.get('IMG_SVR_PRT', "8080")


def string_num_generator(size):
    chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))


@app.route('/')
def hello():
    return stream_template("home.html",
                           rnd=string_num_generator(8),
                           ip=image_server_ip_address,
                           port=image_server_prt_number)

