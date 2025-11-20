from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path


FEATURES = [
    "Close", "Volume", "Open", "High", "Low",
    "Fear_Zscore", "Fear_High", "Fear_STLT_diff",
    "Close_Ratio_2", "Trend_2",
    "Close_Ratio_5", "Trend_5",
    "Close_Ratio_60", "Trend_60",
    "Close_Ratio_250", "Trend_250",
    "Close_Ratio_1000", "Trend_1000",
]

class InputFeatures(BaseModel):
    Close: float
    Volume: float
    Open: float
    High: float
    Low: float
    Fear_Zscore: float
    Fear_High: float
    Fear_STLT_diff: float
    Close_Ratio_2: float
    Trend_2: float
    Close_Ratio_5: float
    Trend_5: float
    Close_Ratio_60: float
    Trend_60: float
    Close_Ratio_250: float
    Trend_250: float
    Close_Ratio_1000: float
    Trend_1000: float

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_methods=["*"],
    allow_headers=["*"],
)