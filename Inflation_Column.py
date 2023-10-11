import requests
from datetime import datetime
import psycopg2

# Set connection with database
conn = psycopg2.connect(database='DB_5', user='postgres', password='Nafay.55', host='localhost', port='5432')

# Getting data from API
url = 'https://www.alphavantage.co/query?function=INFLATION&apikey=JR94ONX7SUG028LJ'
value = requests.get(url)
convert_data = value.json()
data = convert_data['data']

# Getting data from database
cursor_obj = conn.cursor()
cursor_obj.execute('SELECT * FROM public."Data"')
result = cursor_obj.fetchall()

# Getting specific date from data from database
for i in range(len(result)):
    work_year = result[i][0]

    #Getting date from API
    for item in data:
        str_date = item['date']
        api_year = datetime.strptime(str_date, '%Y-%m-%d').date().year
        apivalue = item['value']
        inflation_rate = result[i][-1]

        if api_year == work_year:
            cursor_obj.execute(f'update Data set inflation_rate = {apivalue} where work_year = {work_year};')
            conn.commit()
            print(f'For year "{work_year}" inflation rate value is "{apivalue}"')

# CLose connection with database
cursor_obj.close()
conn.close()
