# Navigating The Financial Markets: ML-Powered Stock Trading and Portfolio Management

## Overview

This GitHub repository contains a Python implementation of an algorithmic trading strategy for navigating financial markets. The strategy utilizes machine learning, specifically TensorFlow, to make trading decisions based on a combination of Exponential Moving Averages (EMA) and Standard Deviation indicators.

The project is structured into modular blocks, each serving a specific purpose in the trading pipeline:

1. **EMA and Standard Deviation Calculation:** Functions to calculate EMA and Standard Deviation for time series data.

2. **Trading Signal Generation:** A function to generate trading signals based on EMA and Standard Deviation indicators.

3. **TensorFlow Model Building and Training:** A function to build and train a simple neural network model using TensorFlow. This model is used to predict buy/sell signals based on historical data.

4. **Risk Management:** A function for applying risk management techniques to control the size of trading positions and protect the capital.

5. **Data Reading:** Code blocks to read financial time series data from CSV files, assumed to be in a specific format.

6. **Execution of Strategy:** Integration of all components to execute the trading strategy on new data.

7. **Visualization:** Visualizing trading signals, price data, and the equity curve with risk management.

## Usage

1. Clone the repository:

```bash
gh repo clone SrikarRavella/Navigating-The-Financial-Markets-ML-Powered-Stock-Trading-and-Portfolio-Management
cd Navigating-The-Financial-Markets-ML-Powered-Stock-Trading-and-Portfolio-Management
```

2. Install the required dependencies:

tensorflow==2.7.0
numpy==1.21.3
pandas==1.3.3
matplotlib==3.4.3

3. Replace the sample CSV files with your actual financial time series data:

   - `training_data.csv`: Historical data used for model training.
   - `new_data.csv`: New data on which the trading strategy will be executed.

## Contributions

Contributions are welcome! If you have ideas for improvements, additional features, or bug fixes, feel free to open an issue or submit a pull request.
