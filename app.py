# heroku logs -a just-a-temp-flask --tail
# heroku logs -a just-a-temp-flask --tail
from flask import Flask, render_template
import matplotlib
import PIL
from histogram_equalization import he

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET', 'PUT'])
def index():
    return render_template('root.html')

@app.route("/he_test", methods = ['POST', 'GET', 'PUT'])
def app_he():
    print("Attempt to to he on " + "input.jpg")
    he("input.jpg")
    print("DONE!!!!")
    return "Hello World!"