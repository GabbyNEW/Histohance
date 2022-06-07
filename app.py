# heroku logs -a just-a-temp-flask --tail
from flask import Flask, render_template, request, redirect, url_for, session
import matplotlib
from PIL import Image
from histogram_equalization import he
import io
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'

@app.route("/", methods = ['POST', 'GET', 'PUT'])
def index():
    if 'input_image' in session : 
        input_image = session['input_image']
        output_image = session['output_image']
    else : 
        input_image = None
        output_image = None
    session.clear()
    return render_template('root.html', input_image=input_image, output_image=output_image)

@app.route("/upload_test", methods = ['POST'])
def he_upload():
    image = request.files["file"]
    image.filename = "input.jpg"
    image.save(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
    perform_he(input_image=image.filename)
    session['input_image'] = image.filename
    session['output_image'] = "output_he.jpeg"
    return redirect(url_for('.index'))

@app.route('/uploads/<filename>')
def send_image_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

def perform_he(input_image):
    # stores the np.array of the output image
    result = he("uploads/"+input_image)
    # convert np.array to .PNG image and save it
    im = Image.fromarray(result)
    im.save('uploads/output_he.jpeg')