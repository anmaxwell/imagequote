from imageclassification import app
from imageclassification.imagemodel import image_select
from flask import render_template, redirect, url_for
import csv
import requests

@app.route('/') #Page to display quote and image
def index():

    scheme = 'http'
    uri = '127.0.0.1'
    port = 5000

    url = f'{scheme}://{uri}:{port}/api/quote'

    quote = requests.get(url)
    quote.raise_for_status()
    text = quote.json()['quote']

    prediction, text = image_select(text)
    background = "%s%s" % (prediction[0], '.jpg')
    #background = '1.jpg'

    return render_template('index.html', background=background, text=text)

@app.route('/addquote/<string:background>/<string:text>') #If the image matches the quote then add to the csv
def add_quote(background, text):

    img_ref = int(background.split(".")[0])

    quote=[img_ref, text]
    with open('imageclassification/imagequotes.csv', 'a') as quotefile:
        writer = csv.writer(quotefile)
        writer.writerow(quote)

    return redirect(url_for('index'))