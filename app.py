from flask import Flask
import cv2 as cv
from numpy.version import release

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
