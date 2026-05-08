'''
🎯 Goal: Predict Quantity

Problem:
Predict Quantity based on Price, Product, Category, City
'''

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('sales_cleaned.csv')

df['Product'] = df['Product'].str.lower()
df['Category'] = df['Category'].str.lower()
df['City'] = df['City'].str.lower()

x = df[['Price', 'Product', 'Category', 'City']]
y = df['Quantity']

'''
Training and testing on SAME data
Model already knows the answers

Train/Test Split:
Split data into training and testing sets
80% train, 20% test

random_state = 42: Ensures same split every run
Without it: train/test rows change every execution
'''

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

'''
our dataset contains text data (categorical data)
but machine learning models like LinearRegression only understand numbers
'''
# ======= Converting text into Numerical Data =======

''' 1) Categorical Columns
Categorical Data: data that represents categories or groups
we tell sklearn: these columns are categorical columns
Price is numeric, so it is NOT being transformed
'''
categorical_features = ['Product', 'Category', 'City']

'''
2) Preprocessing
ColumnTransformer: applies transformations to specific columns
transformers = ['name', encoder, columns]
name: name of transformation (can be anything) ('cat' in our case)
OneHotEncoder(handle_unknown='ignore'): converts text into num
handle_unknown='ignore': handles new values safely
With ignore: model skips unknown category, prediction still works
Without ignore: model throws error if new category appears (crashes)
remainder='passthrough': Keep remaining columns unchanged (Price in our case)
categorical columns → encoded
Price → passed directly
'''
preprocessing = ColumnTransformer(
    transformers = [
        ('cat', OneHotEncoder(handle_unknown = 'ignore'), categorical_features)
    ],
    remainder = 'passthrough'
)
'''
3) Pipeline
Pipeline automatically: Encodes data, Trains model
First convert text columns into numbers using OneHotEncoder
then train LinearRegression on that numeric data.
flow:
Raw Data
   ↓
OneHotEncoder
   ↓
Numeric Data
   ↓
LinearRegression
   ↓
Prediction
'''
model = Pipeline(steps = [
    ('preprocessor', preprocessing),
    ('regressor', LinearRegression())
])

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

# ======= Evaluation =======
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
print(f"Average Quantity: {y.mean():.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")

'''
r2_score (R² Score): how well our model explains the data
Range: 0 → very bad, 1 → perfect model
'''
r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2:.2f}")

'''
which features influence quantity the most
model.named_steps['regressor'].coef_: gives coefficients of features
Positive coefficient → feature increases quantity
Negative coefficient → feature decreases quantity

.named_steps['preprocessor'] accesses the preprocessing step in the pipeline
.get_feature_names_out() returns names of all features after encoding
.named_steps['regressor']: accesses the regression step in the pipeline
.coef_: gives coefficients of all features in the same order
'''
feat = model.named_steps['preprocessor'].get_feature_names_out()
feat = [f.replace('cat__','') for f in feat] # Remove 'cat__' prefix from feature names
coeff = model.named_steps['regressor'].coef_

coef_df = pd.DataFrame({
    'Feature': feat,
    'Coefficient': coeff
})
print("\nFeature Coefficients:")
print(coef_df)

# ======= Visualize Predictions vs Actual =======
'''
r--: red dashed line
This creates the ideal prediction line:
y predicted = y actual
If points lie close to the red dashed line, predictions are accurate
'''
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Quantity')
plt.ylabel('Predicted Quantity')
plt.title('Actual vs Predicted Quantity')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.grid(True)
plt.tight_layout()
plt.show()

# ======= User input =======
print("\nEnter values to get Quantity prediction\n")
price = float(input("Enter Price: "))
product = input("Enter Product: ").lower()
category = input("Enter Category: ").lower()
city = input("Enter City: ").lower()

input_data = pd.DataFrame({
    'Price': [price],
    'Product': [product],
    'Category': [category],
    'City': [city]
})

prediction = model.predict(input_data)
'''
print(f"Predicted Quantity: {round(prediction[0])}")
this might produce 0 or negative values, which doesn't make sense for Quantity
'''
predicted_quantity = max(1, round(prediction[0])) # Ensure at least 1
print(f"Predicted Quantity: {predicted_quantity}")