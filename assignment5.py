#sudo apt-get install python3-dev default-libmysqlclient-dev
#pip install pymysql


from sqlalchemy import create_engine
import pandas as pd

#file path containing credentials


connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connection_string

db = create_engine(connection_string)
print (db.table_names())

r_df = pd.read_csv('data/iris.csv')
r_df.to_sql('dummy_data', con=db, if_exists='replace')

sql_query = 'SELECT * from dummy_data where name="setosa"'

results =pd.read_sql(sql_query, con=db)
results