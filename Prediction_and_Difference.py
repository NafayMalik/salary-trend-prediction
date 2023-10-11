import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from db import db_data

# Assuming your dataset is stored in a DataFrame named 'df'
# If it's not, you can create a DataFrame by reading your data into it.
df = pd.DataFrame(db_data)

# Group by job_title and year
agg_data = df.groupby([0, 3])[[4, 8, 9]].mean().reset_index()

# Set up figure size
from pylab import rcParams
rcParams['figure.figsize'] = 12, 8

# Get unique job_titles and years
job_titles = df[3].unique()
years = df[0].unique()

# Calculate salary trend based on salary_in_usd, inflation_rate, and gdp
agg_data['Salary Trend'] = agg_data[4] - agg_data[8] + agg_data[9]

# Set up figure size for the second plot
plt.figure(figsize=(12, 8))

# Assuming 'work_year' is indexed at 0
X = agg_data[[0]].values
y = agg_data[4].values

# Perform Linear Regression
model = LinearRegression()
model.fit(X, y)

# Predictive years
predictive_years = [2024]  # Add any additional years you want to predict

# Generate data for the predictive years
X_predictive = np.array(predictive_years).reshape(-1, 1)
y_predictive = model.predict(X_predictive)

# Plot the salary trend as a single line
for year in years:
    year_data = agg_data[(agg_data[0] == year)]
    if not year_data.empty:
        plt.plot([f'{year} - {title}' for title in year_data[3]], year_data['Salary Trend'], label=f'Salary Trend - {year}')

# Plot the predicted values
for title in job_titles:
    data_2023 = agg_data[(agg_data[0] == 2023) & (agg_data[3] == title)]
    if not data_2023.empty:
        plt.plot([f'2024 - {title}'], [data_2023['Salary Trend'].values[0]], 'rx')

# Calculate the difference between actual and predicted
difference = y_predictive - y[-1]

# Plot the difference
for title in job_titles:
    data_2023 = agg_data[(agg_data[0] == 2023) & (agg_data[3] == title)]
    if not data_2023.empty:
        plt.plot([f'2024 - {title}'], [data_2023['Salary Trend'].values[0] + difference[0]], 'gs')

# Set labels and title
plt.xlabel('Year and Job Title')
plt.ylabel('Salary')
plt.title('Salary Trend with Predicted Values for 2024')

# Add legend
plt.legend()

# Show the plot
plt.show()
