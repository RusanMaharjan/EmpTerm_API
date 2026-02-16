from fastapi import FastAPI
from models import load_model, features
from schema import EmpTerm
import pandas as pd

app = FastAPI()

model = load_model()

@app.get("/")
def home():
    return {"message": "Welcome to Fast API API."}


@app.get("/api-test")
def api_test():
    return {"message": "This function is to test API."}

@app.post("/predict-termination")
def predict_termination(data: EmpTerm):
    input_data = pd.DataFrame([
        data.dict()
    ], columns=features)

    prediction = model.predict(input_data)[0]
    return {
        "Predicted Termination": int(prediction),
        "Status": "Terminated" if prediction == 1 else "Active"
    }
