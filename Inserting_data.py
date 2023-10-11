import pandas as pd
from sqlalchemy import create_engine

# Define the database connection string. Replace 'your_username', 'your_password', 'your_host', 'your_port',
# and 'your_database' with your Postgresql credentials.
engine = create_engine('postgresql://postgres:Nafay.55@localhost:5432/DB_5')

# Read the CSV file
df = pd.read_csv('ds_salaries.csv')

# Get the column names from the CSV file
columns = list(df.columns)

# Get the table name in your Postgresql database
table_name = 'Data'

# Check if the table exists, if not, create it
with engine.connect() as conn:
    if not engine.dialect.has_table(conn, table_name):
        df.iloc[:0].to_sql(table_name, engine, if_exists='replace', index=False)

# Get the existing columns from the DataFrame
existing_columns = list(df.columns)

# Dynamically alter the table to add columns based on the CSV file
with engine.connect() as conn:
    for col in columns:
        if col not in existing_columns:
            conn.execute(f'ALTER TABLE {table_name} ADD COLUMN "{col}" VARCHAR')

# Insert data into the corresponding columns
df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f'Table "{table_name}" created and data inserted successfully.')

