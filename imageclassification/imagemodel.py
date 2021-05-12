import tensorflow_hub as hub
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def image_select(text:str):

    df = pd.read_csv('imageclassification/imagequotes.csv')

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