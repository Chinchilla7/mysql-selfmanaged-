#sudo apt-get install python3-dev default-libmysqlclient-dev
#pip install pymysql


from sqlalchemy import create_engine
import pandas as pd
from dotenv import dotenv_values

#path containing credentials
config = dotenv_values(".env")

#connect to mysql database using credentials

connection_string = f'mysql+pymysql://{config["MYSQL_USER"]}:{config["MYSQL_PASSWORD"]}@{config["MYSQL_HOSTNAME"]}/{config["MYSQL_DATABASE"]}'
connection_string

db = create_engine(connection_string)
print (db.table_names())

#creating a new table within dummy database called dummy_data containing data from iris csv 
r_df = pd.read_csv('data/iris.csv')
r_df.to_sql('dummy_data', con=db, if_exists='replace')

sql_query = 'SELECT * from dummy_data where name="setosa"'

results =pd.read_sql(sql_query, con=db)
results