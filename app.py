from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

class InputData(BaseModel):
    input1: float
    input2: float

try:
    model = joblib.load('linearModel.pkl')
except Exception as e:
    raise ValueError(f"Error loading the model: {e}")

app = FastAPI()

@app.post("/predict/")

def predict(data: InputData):
    input_values = [[data.input1, data.input2]] 
    prediction = model.predict(input_values)[0]
    return {"Prediction": prediction}


# print(model.predict([[1,2]]))
