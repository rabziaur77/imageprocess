from flask import Flask
import cv2 as cv

app = Flask(__name__)


@app.route("/")
def index():
    img = cv.imread("img.png")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
