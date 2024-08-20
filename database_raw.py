from sqlalchemy import create_engine, Table, Column, Integer,Float, String, MetaData, inspect
import pandas as pd
import json


def credential_loader():
    with open ('credential.json', 'r') as credentials:
        """ Load credentials from json file """
        credential = json.load(credentials)
        username = credential.get('username')
        password = credential.get('password')
        host = credential.get('host')
        port = credential.get('port')
        database = credential.get('database')
    
    return username, password, host, port, database

def create_engine_postgres():
    username, password, host, port, database = credential_loader()
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
    return engine

# Create table in the database
def create_table(engine, df):
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
    
    if not inspect(engine).has_table('candidates_raw'):  # If table don't exist, Create.
        metadata = MetaData()
        columns = [Column(name, infer_sqlalchemy_type(dtype)) for name, dtype in df.dtypes.items()]
        table = Table('candidates_raw', metadata, *columns)
        table.create(engine)
        # Insert data into the table
        df.to_sql('candidates_raw', con=engine, if_exists='append', index=False)
    else:
        print('Table candidates_raw already exists.')


# Check if data is inserted
#query = 'SELECT * FROM candidates_raw'
#data = pd.read_sql_query(query, engine)
#print(data.head())


# Main function to contain the code I want to run
def main():
    df = pd.read_csv('candidates.csv', sep=';')
    engine = create_engine_postgres()
    create_table(engine, df)

if __name__ == '__main__':
    main()