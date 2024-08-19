from sqlalchemy import create_engine, Table, Column, Integer,Float, String, MetaData 
import pandas as pd
import json


df = pd.read_csv('candidates.csv', sep=';')

with open ('credential.json', 'r') as credentials:
    """ Load credentials from json file """
    credential = json.load(credentials)
    username = credential.get('username')
    password = credential.get('password')
    host = credential.get('host')
    port = credential.get('port')
    database = credential.get('database')
    print('Credentials loaded')


engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')


# Create table in the database
metadata = MetaData()

def infer_sqlalchemy_type(dtype):
    """ Map pandas dtype to SQLAlchemy's types """
    if "int" in dtype.name:
        return Integer
    elif "float" in dtype.name:
        return Float
    elif "object" in dtype.name:
        return String(255)
    else:
        return String(255)

columns = [Column(name, infer_sqlalchemy_type(dtype)) for name, dtype in df.dtypes.items()]
table = Table('candidates_raw', metadata, *columns)

table.create(engine)


# Insert data into the table
df.to_sql('candidates_raw', con=engine, if_exists='append', index=False)


# Check if data is inserted
query = 'SELECT * FROM candidates_raw'
data = pd.read_sql_query(query, engine)
print(data.head())