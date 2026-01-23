import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
pd.set_option("display.max_columns", None)

# Load dataset
df = pd.read_csv("audi.csv")

# Prepare features and target
X = df.drop(columns=['price', 'model']) # X is features
y = df['price'] # y is target

# One-hot encode categorical variables
X = pd.get_dummies(X, columns=['transmission', 'fuelType'], drop_first=False, dtype=int)
print(X.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    n_jobs=-1
)

model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)