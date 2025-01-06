# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:06:16 2024

@author: Nester
"""

import json
import requests 

url = 'http://127.0.0.1:8000/heart_disease_prediction'

input_data = {
    'age' : 27 ,
    'sex' : 1 ,
    'cp' : 14 ,
    'trestbps' : 230 ,
    'chol' : 123 ,
    'fbs' : 45 ,
    'restecg'	: 11 ,
    'thalach' : 55 ,
    'exang' : 22 ,
    'oldpeak' : 55.7 ,
    'slope' : 34 ,
    'ca' : 22 ,
    'thal' : 22,
    }

input_json = json.dumps(input_data)

response = requests.post(url, data=input_json)

print(response.text)


