# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("my_first_api")

# Define input model with type annotations
class InputModel(BaseModel):
    season: float
    yr: float
    mnth: float
    hr: float
    holiday: float
    weekday: float
    workingday: float
    weathersit: float
    temp: float
    atemp: float
    hum: float
    windspeed: float

# Define output model with type annotations
class OutputModel(BaseModel):
    prediction: int

# Define predict function
@app.post("/predict", response_model=OutputModel)
def predict(data: InputModel):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
