import pandas as pd
from pylab import rcParams
import matplotlib.pyplot as plt
from db import db_data

# Assuming your dataset is stored in a DataFrame named 'df'
# If it's not, you can create a DataFrame by reading your data into it.
df = pd.DataFrame(db_data)
def get_salary_trend():
    # Group by job_title and year
    agg_data = df.groupby([0, 3])[[4, 8, 9]].mean().reset_index()

    # Set up figure size
    rcParams['figure.figsize'] = 12, 8

    # Get unique job_titles and years
    job_titles = df[3].unique()
    years = df[0].unique()

    # Calculate salary trend based on salary_in_usd, inflation_rate, and gdp
    agg_data['Salary Trend'] = agg_data[4] - agg_data[8] + agg_data[9]

    # Plot the salary trend as a single line
    for year in years:
        year_data = agg_data[(agg_data[0] == year)]
        plt.plot([f'{year} - {title}' for title in year_data[3]], year_data['Salary Trend'],
                 label=f'Salary Trend - {year}')

    # Set labels and title
    plt.xlabel('Year and Job Title')
    plt.ylabel('Salary Trend')
    plt.title('Salary Trend Based on Data')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()

