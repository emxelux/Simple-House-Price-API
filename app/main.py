from fastapi import FastAPI
from app.schema import InputData, PredResponse
import pandas as pd
import pickle as pk

with open("model.pkl", 'rb') as f:
    model = pk.load(f)

app = FastAPI()

@app.get('/')
def homepage():
    return {"message":'Welcome to House price prediction'}

@app.post('/predict', response_model=PredResponse)
async def predict_price(house_data: InputData):
    df = pd.DataFrame([house_data.dict()])
    pred = model.predict(df)
    return {'Price': f"The Likely Price of the house you want is {pred.round(2)}"}
