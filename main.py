from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated
from fastapi.responses import JSONResponse
import pickle
import pandas as pd 

app = FastAPI()


# Nitrogen	Phosphorus	Potassium	Temperature	Humidity	pH_Value	Rainfall	Crop
class schema(BaseModel):
    Nitrogen: Annotated[int, Field(ge=0, le=140, description="Nitrogen content in the soil", example=45)]
    Phosphorus: Annotated[int, Field(ge=5, le=145, description="Phosphorus content in the soil", example=30)]
    Potassium: Annotated[int, Field(ge=5, le=145, description="Potassium content in the soil", example=50)]
    Temperature: Annotated[float, Field(ge=8, le=44, description="Temperature in degrees Celsius", example=30.0)]
    Humidity: Annotated[float, Field(ge=14, le=100, description="Humidity percentage", example=70.0)]
    pH_Value: Annotated[float, Field(ge=3, le=10, description="pH value of the soil", example=6.5)]
    Rainfall: Annotated[float, Field(ge=100, le=300, description="Rainfall in millimeters", example=100.0)]


def load_model():
    with open('best_model_pipeline.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


@app.get("/")
def read_root():
     return {"message": "Crop Prediction API"}


@app.post("/predict")
def predict_crop(data: schema):
    model = load_model()
    
    # Prepare input as a DataFrame with correct column names
    input_df = pd.DataFrame([{
        'Nitrogen': data.Nitrogen,
        'Phosphorus': data.Phosphorus,
        'Potassium': data.Potassium,
        'Temperature': data.Temperature,
        'Humidity': data.Humidity,
        'pH_Value': data.pH_Value,
        'Rainfall': data.Rainfall
    }])
    
    try:
        prediction = model.predict(input_df)
        predicted_crop = prediction[0]
        return JSONResponse(content={"predicted_crop": predicted_crop}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

