# heroku logs -a just-a-temp-flask --tail
# heroku logs -a just-a-temp-flask --tail
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET', 'PUT'])
def index():
    return render_template('root.html')