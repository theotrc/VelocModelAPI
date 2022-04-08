# from crypt import methods
from flask import Flask
from flask import Blueprint, request
import requests
import sklearn
from lightgbm import LGBMRegressor
import json
import pickle
import pandas as pd
import numpy as np


# openmodel = open("App/routes/model.pkl", "rb")
openmodel = open("App/routes/model_rf.pkl", "rb")

model = pickle.load(openmodel)

model_ml = Blueprint("model_ml", __name__, static_folder="../static", template_folder="../templates/")
@model_ml.route('/')
def runing():
    

    return '<h1> run </h1>'


    
@model_ml.route('/predict', methods=['get', 'post'])
def predict_page():
    print('record : ', request.json)
    record = request.json
    features = ['holiday', 'workingday', 'weather', 'temp', 'humidity', 'windspeed', 'month', 'hours','weekday','year']
    df = pd.DataFrame()
    
    value= []
    for col in features:
        value.append(record[col])

    df[features] = [np.array(value)]
    df = df.astype({'holiday': 'int64', 'workingday' : 'int64', 'weather': 'int64',
    'temp' : 'float64', 'humidity':'int64', 'windspeed':'float64', 'month':'int64', 'hours':'int64', 'weekday':'int64', 'year':'int64'})
    print('df ta mere: ' , df.dtypes)
    prediction = model.predict(df)
    
    print(prediction[0])

    return str(int(prediction[0]))



