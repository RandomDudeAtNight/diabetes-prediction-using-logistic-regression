from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pickle
import pandas as pd
import numpy as np
from typing import Optional

# Initialize FastAPI app
app = FastAPI(
    title="Diabetes Prediction API",
    description="API for predicting diabetes using logistic regression model",
    version="1.0.0"
)

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model at startup
try:
    model = pickle.load(open('logistic_regression_model.pkl', 'rb'))
except FileNotFoundError:
    print("Warning: Model file not found. Please ensure 'logistic_regression_model.pkl' is in the same directory.")
    model = None

# Define the input data model
class PatientData(BaseModel):
    Pregnancies: int = Field(..., ge=0, description="Number of pregnancies")
    Glucose: float = Field(..., ge=0, description="Glucose level")
    BloodPressure: float = Field(..., ge=0, description="Blood pressure")
    SkinThickness: float = Field(..., ge=0, description="Skin thickness")
    Insulin: float = Field(..., ge=0, description="Insulin level")
    BMI: float = Field(..., ge=0, description="Body Mass Index")
    DiabetesPedigreeFunction: float = Field(..., ge=0, description="Diabetes pedigree function")
    Age: int = Field(..., ge=0, description="Age in years")

    class Config:
        json_schema_extra = {
            "example": {
                "Pregnancies": 1,
                "Glucose": 120,
                "BloodPressure": 70,
                "SkinThickness": 30,
                "Insulin": 0,
                "BMI": 25.5,
                "DiabetesPedigreeFunction": 0.3,
                "Age": 22
            }
        }

# Define the response model
class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    message: str
    input_data: dict

@app.get("/")
async def root():
    """Root endpoint to check if API is running"""
    return {
        "message": "Diabetes Prediction API is running",
        "status": "healthy",
        "endpoints": {
            "predict": "/predict",
            "health": "/health",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict_diabetes(patient: PatientData):
    """
    Predict diabetes for a patient based on their medical data
    
    Returns:
    - prediction: 0 (no diabetes) or 1 (has diabetes)
    - probability: probability of having diabetes
    - message: human-readable prediction result
    """
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Please check server configuration.")
    
    try:
        # Convert input data to DataFrame
        input_dict = patient.dict()
        patient_df = pd.DataFrame([input_dict])
        
        # Make prediction
        prediction = model.predict(patient_df)[0]
        
        # Get probability (if model supports predict_proba)
        try:
            probability = model.predict_proba(patient_df)[0][1]  # Probability of class 1 (diabetes)
        except AttributeError:
            probability = float(prediction)  # Fallback if predict_proba not available
        
        # Generate message
        if prediction == 1:
            message = "The model predicts that the patient is likely to have diabetes."
        else:
            message = "The model predicts that the patient is likely not to have diabetes."
        
        return PredictionResponse(
            prediction=int(prediction),
            probability=float(probability),
            message=message,
            input_data=input_dict
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
