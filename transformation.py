import pandas as pd
import numpy as np
from sqlalchemy import create_engine, Table, Column, Integer,Float, String, MetaData, inspect
from database_raw import credential_loader, create_engine_postgres

#Este código se me ocurrió pero no es para nada optimo, lo dejo comentado para que veas que se me ocurrió.

#for i in data['Technical Interview Score']:
#    for e in data['Code Challenge Score']:
#        if i >= 7 and e >= 7:
#            data['is_hired'] = 'Hired'
#        else:
#            data['is_hired'] = 'Not Hired'

def limpieza_general(data):
    data.dropna(inplace=True)
    data['Application Date'] = pd.to_datetime(data['Application Date'])
    data['is_hired'] = np.where((data['Technical Interview Score'] >= 7) & (data['Code Challenge Score'] >= 7), 'Hired', 'Not Hired')
    if data.duplicated().sum() > 0:
        data.drop_duplicates(inplace=True)
    
    return data

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
    
    if not inspect(engine).has_table('candidates_cleaned'):  # If table don't exist, Create.
        metadata = MetaData()
        columns = [Column(name, infer_sqlalchemy_type(dtype)) for name, dtype in df.dtypes.items()]
        table = Table('candidates_cleaned', metadata, *columns)
        table.create(engine)
        # Insert data into the table
        df.to_sql('candidates_cleaned', con=engine, if_exists='append', index=False)
    else:
        print('Table candidates_cleaned already exists.')


def main():
    engine = create_engine_postgres()
    df = pd.read_sql_query('SELECT * FROM candidates_raw', engine)
    df = limpieza_general(df)
    create_table(engine, df)

if __name__ == '__main__':
    main()