FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY imageclassification imageclassification

ENV FLASK_APP=imageclassification
ENV FLASK_ENV=development

CMD [ "flask", "run", "--host=0.0.0.0" ,  "--port=8000" ]