# S&P 500 Direction Predictor

**Author:**

Christopher Benjamin

Computer Science B.S. student @ University of California, Irvine

---

A machine learning project that forecasts **next-day S&P 500 movement** (up or down) using historical market data and volatility indicators.  
The model combines **technical**, **trend**, and **sentiment (VIX/Fear Index)** features to evaluate directional probabilities with walk-forward backtesting.

---

## Overview

This notebook builds and evaluates predictive models for the S&P 500 index (^GSPC) using a data-driven, time-aware pipeline:

- **Data Source:** Yahoo Finance (via `yfinance`)
- **Features:**  
  - OHLCV data (Open, High, Low, Close, Volume)  
  - VIX-based “Fear Index” metrics (z-score, high-vol indicator, short/long-term spread)  
  - Rolling ratios and trend counts over multiple horizons  
- **Target:** Binary variable — 1 if the next day’s close > today’s, else 0

---

## Features & Engineering

| Category | Description |
|-----------|-------------|
| **Price Ratios** | Close price divided by its rolling mean across 2, 5, 60, 250, and 1000 days |
| **Trend Counts** | Number of recent up-days in the same windows |
| **Fear Index** | Derived from VIX: z-score deviation, short-term vs long-term difference, and “high-vol” flag |
| **Base Inputs** | Close, Volume, Open, High, Low |

---

## Modeling Pipeline

- **Algorithms:**  
  - Random Forest Classifier (tuned via GridSearchCV)  
  - Logistic Regression baseline  
- **Evaluation:**  
  - Walk-forward cross-validation using `TimeSeriesSplit`  
  - Precision, recall, and F1 metrics across probability thresholds  
- **Key Metric:**  
  - *Precision on out-of-sample predictions* — headline measure of model success  

---

## Backtesting Framework

The project uses a **rolling (walk-forward) backtest**:
1. Train on all available data up to a point (`start` index).  
2. Test on the following `step`-sized window (e.g., 250 days).  
3. Expand training window and repeat.  

This prevents data leakage and simulates real-world deployment.



