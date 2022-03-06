from flask import Flask
import cv2 as cv

app = Flask(__name__)


@app.route("/")
def index():
    img = cv.version.opencv_version
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return img


if __name__ == "__main__":
    app.run(debug=True)
