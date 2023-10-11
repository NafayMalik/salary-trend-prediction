import pandas as pd
from pylab import rcParams
import matplotlib.pyplot as plt
from db import db_data

# Assuming your dataset is stored in a DataFrame named 'df'
# If it's not, you can create a DataFrame by reading your data into it.
df = pd.DataFrame(db_data)

# Define the job title you're interested in
job_title = 'Data Scientist'

# Filter data for a specific job_title
df_filtered = df[df[3] == job_title]

# Group by job_title and year
agg_data = df_filtered.groupby([0, 3])[[4, 8, 9]].mean().reset_index()

# Set up figure size
rcParams['figure.figsize'] = 12, 8

# Calculate salary trend based on salary_in_usd, inflation_rate, and gdp
agg_data['Salary Trend'] = agg_data[4] - agg_data[8] + agg_data[9]

# Plot the salary trend as a single line
plt.plot([f'{year} - {title}' for year, title in zip(agg_data[0], agg_data[3])], agg_data['Salary Trend'], label=f'Salary Trend')

# Set labels and title
plt.xlabel('Year and Job Title')
plt.ylabel('Salary Trend')
plt.title(f'Salary Trend for {job_title}')


# Add legend
plt.legend()

# Show the plot
plt.show()
