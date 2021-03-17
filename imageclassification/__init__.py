import os
from flask import Flask

app = Flask(__name__)

#to prevent getting stuck in circular imports create this last
from imageclassification import routes