# heroku logs -a just-a-temp-flask --tail
from enum import auto
from flask import Flask, render_template, request, redirect, url_for, session
import matplotlib
from PIL import Image
from histogram_equalization import he
from dynamic_histogram_equalization import dhe
import io
from werkzeug.utils import secure_filename
import os

# Define the static and uploads directories
UPLOAD_FOLDER = 'uploads/'
STATIC_FOLDER = 'static/'
app = Flask(__name__, static_folder=STATIC_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'super secret key'

# Ask if the server user wants to use TEMPLATES_AUTO_RELOAD
# autoReloadEnabled = True if str(input("Do you want templates to automatically reload when they are changed? (Y/N): ")).lower() == 'y' else False
# app.config['TEMPLATES_AUTO_RELOAD'] = autoReloadEnabled
# print("Running with auto reload " + "enabled" if str(autoReloadEnabled) else "disabled")

# Routing
@app.route("/", methods = ['POST', 'GET', 'PUT'])
def index():
    return render_template('index.html')

@app.route("/he", methods = ['POST', 'GET', 'PUT'])
def he_web():
    if 'input_image' in session : 
        input_image = session['input_image']
        output_image = session['output_image']
    else : 
        input_image = None
        output_image = None
    session.clear()
    return render_template('he.html', input_image=input_image, output_image=output_image)

@app.route("/dhe", methods = ['POST', 'GET', 'PUT'])
def dhe_web():
    if 'input_image' in session :
        input_image = session['input_image']
        output_image = session['output_image']
    else :
        input_image = None
        output_image = None
    session.clear()
    return render_template('dhe.html', input_image=input_image, output_image=output_image)

@app.route("/he_upload", methods = ['POST'])
def he_upload():
    image = request.files["file"]
    image.filename = "input.jpg"
    image.save(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
    perform_he(input_image=image.filename)
    session['input_image'] = image.filename
    session['output_image'] = "output_he.jpeg"
    return redirect(url_for('.he_web'))

@app.route("/dhe_upload", methods= ['POST'])
def dhe_upload():
    size = 480, 480
    image = request.files["file"]
    im = Image.open(image)
    im.filename = "input.jpg"
    im.thumbnail(size, Image.ANTIALIAS)
    width, height = im.size
    print("Image resized to " + str(width) + "x" + str(height))
    im.save(os.path.join(app.config["UPLOAD_FOLDER"], im.filename))
    perform_dhe(input_image=im.filename)
    session['input_image'] = im.filename
    session['output_image'] = "output_dhe.jpeg"

    # return redirect(url_for('.dhe_web'))
    return "Success"

@app.route('/uploads/<filename>')
def send_image_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route('/downloads/<filename>')
def download_image_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

def perform_he(input_image):
    # stores the np.array of the output image
    result = he("uploads/"+input_image)
    # convert np.array to .PNG image and save it
    im = Image.fromarray(result)
    im.save('uploads/output_he.jpeg')

def perform_dhe(input_image):
    # stores the np.array of the output image
    result = dhe("uploads/"+input_image)
    # convert np.array to .PNG image and save it
    im = Image.fromarray(result)
    im.save('uploads/output_dhe.jpeg')