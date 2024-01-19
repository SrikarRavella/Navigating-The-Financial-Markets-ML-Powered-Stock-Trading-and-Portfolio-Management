from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity. Narrow it down in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (for serving a frontend, if needed)
app.mount("/", StaticFiles(directory="static", html=True), name="static")


class PredictionRequest(BaseModel):
    new_data: pd.DataFrame


class PredictionResponse(BaseModel):
    buy_signals: list
    sell_signals: list
    equity_curve: list


# Load the trained model
model = load_model("trained_model.h5")  # Replace with the actual path to your trained model file


@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    new_data = request.new_data
    new_price_data = new_data['Close'].values

    # Assume you have functions for generating signals and applying risk management
    new_signals = generate_signals(new_price_data, ema_window_size, std_window_size)
    new_positions = execute_strategy(model, new_signals)
    new_equity_curve = apply_risk_management(new_positions, new_price_data)

    return PredictionResponse(
        buy_signals=list(np.where(new_positions == 1)[0]),
        sell_signals=list(np.where(new_positions == -1)[0]),
        equity_curve=list(new_equity_curve)
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)