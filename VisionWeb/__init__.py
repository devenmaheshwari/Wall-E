# Wall-E: Deven Maheshwari, Aaron Contreras, Brigid Allen
# Google Mentorship
# Web App
# June 20 2022

from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append("/var/www/FlaskApp/VisionWeb")

# boilerplate code
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)