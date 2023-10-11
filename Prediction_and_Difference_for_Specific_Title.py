import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from db import db_data
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
def generate_salary_plot(job_title: str):
    # Assuming your dataset is stored in a DataFrame named 'df'
    # If it's not, you can create a DataFrame by reading your data into it.
    df = pd.DataFrame(db_data)

    # Filter data for a specific job_title
    # job_title = 'Data Scientist'  # Replace with the specific job title you're interested in
    df_filtered = df[df[3] == job_title]

    # Group by the relevant columns (work_year) and calculate averages
    agg_data = df_filtered.groupby([0])[[4, 8, 9]].mean().reset_index()

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
    print(f'predictive value {y_predictive}')
    # Set up figure size
    plt.figure(figsize=(12, 8))

    # Plot the original data
    years = agg_data[0].unique()
    plt.plot(years, y, label='Actual Salary', marker='o')

    # Plot the predicted values
    plt.plot(predictive_years, y_predictive, label='Predicted Salary', marker='x')

    # Calculate the difference between actual and predicted
    difference = y_predictive - y[-1]
    print(f'Difference between predictive value and actual value{difference}')
    # Plot the difference
    plt.plot(predictive_years, [difference[0]], label='Difference', marker='s')

    # Set x-axis ticks to your specific years
    plt.xticks(years.tolist() + predictive_years)
    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Salary')
    plt.title(f'Actual vs. Predicted Salary for 2024 for {job_title}')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()

    # Convert the plot to a PNG image
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Save the plot as a PNG
    plt.savefig('salary_plot.png')

    # Get the data points for every year along with salary
    salary_data = []
    for year, salary in zip(years, y):
        salary_data.append({"Year": int(year), "Salary": float(salary)})

    # Get the printed output
    printed_output = {
        "Predictive Value": float(y_predictive[0]),
        "Difference": float(difference[0])
    }


    return buffer, printed_output, salary_data

