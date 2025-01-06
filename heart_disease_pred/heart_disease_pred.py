from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import numpy as np
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
@app.get("/", response_class=HTMLResponse)
def read_index():
    return """
    <html>
        <head>
            <title>Hello Page</title>
        </head>
        <body>
            <h1>Welcome to heart disease api</h1>
        </body>
    </html>
    """


@app.post('/heart_disease_prediction')
def heart_disease_pred(input_parameters: model_input):
    input_data = input_parameters.dict()
    input_list = list(input_data.values())
    input_array = np.array(input_list).reshape(1, -1)

    Prediction = heart_disease_model.predict(input_array)

    # Return a structured JSON response
    result = {
        "prediction": "High probability of having a heart disease" if Prediction[0] == 1 else "Low probability of having a heart disease"
    }
    return result
