# Fuel Consumption Prediction using Linear Regression and FastAPI

This project aims to predict fuel consumption based on vehicle attributes using a linear regression model and deploy it as a FastAPI application.

## Dataset
The dataset used in this project is the "fuelconsumption" dataset. It contains information about various attributes of vehicles and their corresponding fuel consumption rates. The dataset is available in the repository.

## Dependencies
- Python 3.x
- scikit-learn
- pandas
- numpy
- fastapi
- uvicorn

Install dependencies using:
```bash
pip install -r requirements.txt
````
## Project Structure

```` 
fuel-consumption-prediction/
│
├── data/
│   ├── fuel_consumption.csv        # Dataset
│
├── models/
│   ├── fuel_consumption_model.pkl  # Trained model
│
├── app.py                          # FastAPI application
├── main.ipynb  # Jupyter notebook for data exploration and model training
├── requirements.txt                # Dependencies
└── README.md                       # Project documentation

````