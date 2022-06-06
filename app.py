# heroku logs -a just-a-temp-flask --tail
# heroku logs -a just-a-temp-flask --tail
from flask import Flask, render_template
import matplotlib

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET', 'PUT'])
def index():
    print(matplotlib.__name__)
    return render_template('root.html')