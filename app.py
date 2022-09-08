from flask import Flask, stream_template
import random
import string

app = Flask(__name__)


def string_num_generator(size):
    chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))


@app.route('/')
def hello():
    return stream_template("home.html", rnd=string_num_generator(8))

