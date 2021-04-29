import tensorflow as tf
import tensorflow_hub as hub
import csv
import string
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def image_select():

    df = pd.read_csv('imageclassification/imagequotes.csv')
    text = 'As human beings our greatness lies not so much in being able to remake the world - that is the myth of the atomic age - as in being able to remake ourselves.'

    module_url = 'https://tfhub.dev/google/universal-sentence-encoder/4'
    model = hub.load(module_url)

    df['Vector'] = model(df['Quote'])

    dataset = pd.DataFrame(df['Vector'].tolist(), index=df.index)

    X = dataset
    y = df['Image']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    knn_classifier = KNeighborsClassifier()
    knn_classifier.fit(X_train, y_train)

    quote = model([text])
    knn_predictions = knn_classifier.predict(quote)

    return knn_predictions, text