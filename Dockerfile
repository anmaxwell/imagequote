FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY imageclassification imageclassification

ENV FLASK_APP=imageclassification
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=8000

# ENV QUOTEMAKER_API_SCHEME=http
# ENV QUOTEMAKER_API_URI=127.0.0.1
# ENV QUOTEMAKER_API_PORT=5000

CMD [ "flask", "run", "--host=0.0.0.0" ]