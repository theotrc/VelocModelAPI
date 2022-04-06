# from crypt import methods
from flask import Flask
from flask import Blueprint, request
import requests
import sklearn
import json
import pickle
import pandas as pd
import numpy as np


openmodel = open("App/routes/model.pkl", "rb")

model = pickle.load(openmodel)

model_ml = Blueprint("model_ml", __name__, static_folder="../static", template_folder="../templates/")
@model_ml.route('/')
@model_ml.route('/predict', methods=['get', 'post'])
def predict_page():
    print('record : ', request.json)
    record = request.json
    features = ['holiday', 'workingday', 'weather', 'temp', 'humidity', 'windspeed', 'month', 'hours','week']
    df = pd.DataFrame()
    
    value= []
    for col in features:
        value.append(record[col])
    # df = pd.DataFrame(record, orient='index',  columns=[features])
    df[features] = [np.array(value)]
    df = df.astype({'holiday': 'int64', 'workingday' : 'int64', 'weather': 'int64',
    'temp' : 'float64', 'humidity':'int64', 'windspeed':'float64', 'month':'int64', 'hours':'int64'})
    print('df ta mere: ' , df.dtypes)
    # print(df)
    # np.array(df).reshape(1, 1)
    prediction = model.predict(df)
    
    print(prediction[0])

    return str(int(prediction[0]))



