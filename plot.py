import pandas as pd
import matplotlib.pyplot as plt
from db import db_data

# Assuming your dataset is stored in a DataFrame named 'df'
# If it's not, you can create a DataFrame by reading your data into it.
df = pd.DataFrame(db_data)

# Group by job_title
agg_data = df.groupby([0, 3])[[4, 8, 9]].mean().reset_index()

# Set up figure size
from pylab import rcParams
rcParams['figure.figsize'] = 12, 8

# Get unique job_titles and years
job_titles = df[3].unique()
years = df[0].unique()

# Initialize a dictionary to store the column indices for each metric
metric_indices = {'Salary': 4, 'Inflation Rate': 8, 'GDP': 9}

# Plot the data for each metric as a single line
for metric, col_index in metric_indices.items():
    for year in years:
        year_data = agg_data[(agg_data[0] == year)]
        plt.plot([f'{year} - {title}' for title in year_data[3]], year_data[col_index], label=f'{metric}')

# Set labels and title
plt.xlabel('Year and Job Title')
plt.ylabel('Average')
plt.title('Average Metrics Comparison')

# Add legend
plt.legend()

# Show the plot
plt.show()
