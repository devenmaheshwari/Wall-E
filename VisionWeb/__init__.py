# Wall-E: Deven Maheshwari, Aaron Contreras, Brigid Allen
# Google Mentorship
# Web App
# June 20 2022

from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import numpy as np
from flask_ngrok import run_with_ngrok
import os

import sys
sys.path.append("/var/www/FlaskApp/VisionWeb")

from google.colab import drive
drive.mount('/content/gdrive')
PEOPLE_FOLDER = os.path.join('static', 'people_photo')

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
run_with_ngrok(app)

# boilerplate code
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/how", methods=["GET"])
def how():
    return render_template('how.html')


@app.route("/demo", methods=["GET", "POST"])
def appfunction():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Shovon.jpg')
    return render_template('Webp.html',user_image = full_filename)
    return render_template('demo.html')


@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)





