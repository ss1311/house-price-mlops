import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("model.joblib")

class HouseData(BaseModel):
    bedrooms: float
    bathrooms: float
    sqft_living: int
    sqft_lot: int
    floors: float
    waterfront: int
    view: int
    condition: int
    sqft_above: int
    sqft_basement: int
    yr_built: int
    yr_renovated: int
    city: str
    statezip: str

@app.get("/")
def home():
    return {"message": "House Price Prediction API running"}

@app.post("/predict")
def predict(data: HouseData):
    df = pd.DataFrame([data.model_dump()])
    price = model.predict(df)[0]
    return {"predicted_price": round(float(price), 2)}