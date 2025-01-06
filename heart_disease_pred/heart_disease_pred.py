# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:52:42 2024

@author: Nester
"""

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    
    age : int 
    sex : int 
    cp : int 
    trestbps : int 
    chol : int 
    fbs : int 
    restecg	: int 
    thalach : int 
    exang : int 
    oldpeak : float 
    slope : int 
    ca : int 
    thal : int
    
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))


@app.post('/heart_disease_prediction')
def heart_disease_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dict = json.loads(input_data)
    
    age = input_dict['age']
    sex = input_dict['sex']
    cp = input_dict['cp']
    trestbps = input_dict['trestbps']
    chol = input_dict['chol']
    fbs = input_dict['fbs']
    restecg = input_dict['restecg']
    thalach = input_dict['thalach']
    exang = input_dict['exang']
    oldpeak = input_dict['oldpeak']
    slope = input_dict['slope']
    ca = input_dict['ca']
    thal = input_dict['thal']
    
    input_list = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    input_list = np.array(input_list).reshape(1, -1)

    Prediction = heart_disease_model.predict(input_list)
    
    
    if(Prediction[0] == 1):
        return 'High probability of having a heart disease'
    else:
        return 'Low probability of having a heart disease'
    







