import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<path:ignore>')
def hihelo(ignore="mr gray"):
	return f"hi helo {ignore} {time.time()}"
