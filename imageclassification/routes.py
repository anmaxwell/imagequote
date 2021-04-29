from imageclassification import app
from imageclassification.imagemodel import image_select
from flask import render_template
from random import randrange

@app.route('/') #Page to display quote and image
def index():

    prediction, text = image_select()
    background = "%s%s" % (prediction[0], '.jpg')

    #text = 'As human beings our greatness lies not so much in being able to remake the world - that is the myth of the atomic age - as in being able to remake ourselves.'
    #background = '1.jpg'

    return render_template('index.html', background=background, text=text)