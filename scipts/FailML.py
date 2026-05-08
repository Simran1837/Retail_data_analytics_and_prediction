'''
Revenue = Price × Quantity
is already a known deterministic formula
There is no hidden pattern to learn

Linear Regression tries to learn relationships like:
Revenue= m1(Price)+m2(Quantity)+c

But your real relationship is:
Revenue=Price×Quantity

That is: multiplicative, exact, already known
So ML becomes unnecessary
'''
# Linear regression on rev = price x qty is a bad idea
# because the relationship is multiplicative, not additive

# Below code only available for demonstration and learning purposes

'''
🎯 Goal: Predict Sales

Problem:
Predict Revenue based on Price & Quantity
'''

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('sales_cleaned.csv')

x = df[['Price', 'Quantity']]
y = df['Revenue']

'''Problem:
Training and testing on SAME data
Model already “knows” the answers

Train/Test Split:
Split data into training and testing sets
80% train, 20% test
'''
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test) # test on unseen data

'''
MSE (Mean Squared Error):
Measures average error in prediction 
MSE = average of (Actual - Predicted)²
Low MSE → good model ✅
High MSE → bad model ❌
RMSE: brings error back to same unit as Revenue
comparing RMSE vs avg revenue
'''
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"Average Revenue: {y.mean():.2f}")
print(f"RMSE: {rmse:.2f}")

print("Enter Price and Quantity to predict Future Revenue\n")
a = float(input("Enter Price: "))
b = int(input("Enter Quantity: "))
if a <= 0 or b <= 0:
    print("Price and Quantity must be greater than 0!")
    exit()


print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

'''
r2_score (R² Score):
how well our model explains the data
Range: 0 → very bad, 1 → perfect model
'''
r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2:.2f}")

'''
model expects 2d data and our training data is a numpy array 
So prediction should match same format
and ML pipelines always use NumPy arrays
'''
model_pred = model.predict(np.array([[a,b]]))
print(f"Predicted Revenue for Price {a} and Quantity {b} is: {model_pred[0]:.2f}")

