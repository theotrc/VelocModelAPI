from crypt import methods
from flask import Flask
from flask import Blueprint, request
import requests


model_ml = Blueprint("model_ml", __name__, static_folder="../static", template_folder="../templates/")
@model_ml.route('/')
@model_ml.route('/predict', methods=['get', 'post'])
def predict_page():

    x = requests.get('http://127.0.0.1:5000/formulaire')
    print(x)
    return x



