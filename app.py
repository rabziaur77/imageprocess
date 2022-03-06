from flask import Flask
import cv2 as cv

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
