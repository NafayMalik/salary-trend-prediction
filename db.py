import psycopg2

# Set connection with database
conn = psycopg2.connect(database='DB_5', user='postgres', password='Nafay.55', host='localhost', port='5432')

# Getting data from database
cursor_obj = conn.cursor()
cursor_obj.execute('select * from public.data')
db_data = cursor_obj.fetchall()
