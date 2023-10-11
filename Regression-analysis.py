
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
from db import db_data

# Assuming your dataset is stored in a DataFrame named 'df'
# If it's not, you can create a DataFrame by reading your data into it.
df = pd.DataFrame(db_data)
X = df[[4, 8, 9]]
y = df[4]

#Split data into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Perform Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

#Make Predictions
y_pred = model.predict(X_test)

#Calculating mean 'squared error'
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Calculating R-squared (Coefficient of Determination)
r_squared = r2_score(y_test, y_pred)
print(f"R-squared: {r_squared}")

# Assuming p is the number of predictors
p = X.shape[1]
n = len(y_test)
adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)
print(f"Adjusted R-squared: {adjusted_r_squared}")

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae}")

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Squared Error (RMSE): {rmse}")

#Create a scatter plot to visually inspect how well the model's predictions align with the actual values.
plt.scatter(y_test, y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs. Predicted")
plt.show()

