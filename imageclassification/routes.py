from imageclassification import app
from imageclassification.imagemodel import image_select
from flask import render_template, redirect, url_for
import csv

@app.route('/') #Page to display quote and image
def index():

    #prediction, text = image_select()
    #background = "%s%s" % (prediction[0], '.jpg')

    text = 'As human beings our greatness lies not so much in being able to remake the world - that is the myth of the atomic age - as in being able to remake ourselves.'
    background = '1.jpg'

    return render_template('index.html', background=background, text=text)

@app.route('/addquote/<string:background>/<string:text>') #If the image matches the quote then add to the csv
def add_quote(background, text):

    img_ref = int(background.split(".")[0])

    quote=[img_ref, text]
    with open('imageclassification/imagequotes.csv', 'a') as quotefile:
        writer = csv.writer(quotefile)
        writer.writerow(quote)

    return redirect(url_for('index'))