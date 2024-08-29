from function.database.database import create_engine_postgres, create_table
import pandas as pd


# Check if data is inserted
#query = 'SELECT * FROM candidates_raw'
#data = pd.read_sql_query(query, engine)
#print(data.head())


# Main function to contain the code I want to run
def main():
    df = pd.read_csv('data/raw/candidates.csv', sep=';')
    engine = create_engine_postgres()
    create_table(engine, df, 'candidates_raw')

if __name__ == '__main__':
    main()