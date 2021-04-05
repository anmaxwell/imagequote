from imageclassification import app
from flask import render_template
from random import randrange

@app.route('/') #Page to display quote and image
def index():

    image = randrange(1,22) 
    background = "%s%s" % (image, ".jpg")

    return render_template('index.html', background=background)