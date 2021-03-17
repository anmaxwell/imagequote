from imageclassification import app
from flask import render_template

@app.route('/') #Page to display quote and image
def index():

    return render_template('index.html')