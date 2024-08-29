from sqlalchemy import create_engine, Table, Column, Integer,Float, String, MetaData, inspect, DateTime
import json

def create_table(engine, df, table_name):
    if not inspect(engine).has_table(table_name):  # If table don't exist, Create.
        metadata = MetaData()
        columns = [Column(name, infer_sqlalchemy_type(dtype)) for name, dtype in df.dtypes.items()]
        table = Table(table_name, metadata, *columns)
        table.create(engine)
        # Insert data into the table
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
    else:
        print(f'Table {table_name} already exists.')


def credential_loader():
    with open ('./credentials/credential.json', 'r') as credentials:
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


#Define function to infer the SQL type from pandas type
def infer_sqlalchemy_type(dtype):
    """ Map pandas dtype to SQLAlchemy's types """
    if "int" in dtype.name:
        return Integer
    elif "float" in dtype.name:
        return Float
    elif "object" in dtype.name:
        return String(255)
    elif "datetime" in dtype.name:
        return DateTime
    else:
        return String(255)