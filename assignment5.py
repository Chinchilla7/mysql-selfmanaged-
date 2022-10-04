#sudo apt-get install python3-dev default-libmysqlclient-dev
#pip install pymysql

from os import environ
from sqlalchemy import create_engine
import pandas as pd

#file path containing credentials

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connection_string

db = create_engine(connection_string)

r_df = pd.read_csv('')
r_df.to_sql('dummy_data', con=db, if_exists='replace')

sql_query = """select * from dummy_data where gender = 'Male'"""