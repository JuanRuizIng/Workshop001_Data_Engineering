import pandas as pd
import numpy as np
from function.database.database import create_engine_postgres, create_table

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
    data['is_hired'] = np.where((data['Technical Interview Score'] >= 7) & (data['Code Challenge Score'] >= 7), 1, 0)
    if data.duplicated().sum() > 0:
        data.drop_duplicates(inplace=True)
    
    return data


def main():
    engine = create_engine_postgres()
    df = pd.read_sql_query('SELECT * FROM candidates_raw', engine)
    df = limpieza_general(df)
    create_table(engine, df, 'candidates_cleaned')

if __name__ == '__main__':
    main()