
import pandas as pd
from sqlalchemy import create_engine

def treat_companies():
    # dialect+driver://username:password@host:port/database
    engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres/postgres")

    data = ''

    with open ('./data/csv/companies.csv', encoding='utf-8') as f:
        data = f.read()
        data = data.replace(' ; ', ';').replace(' ;', ';').replace('; ', ';').replace(';-;', ';;'). \
            replace('; - ;', ';;')
        
        data = data.replace(' ; ', ';').replace(' ;', ';').replace('; ', ';').replace(';-;', ';;'). \
            replace('; - ;', ';;')
        
        data = data.replace('R$ ', '').replace('R$', '').replace('%', '')

        data = data.replace('.', '').replace(';-;', ';;')

        data = data.replace(',', '.').replace(';-;', ';;')


    with open ('./data/csv/companies_treated.csv', 'w', encoding='utf-8') as f:
        f.write(data)


    df = pd.read_csv('./data/csv/companies_treated.csv', sep=';', encoding='utf-8')


    df.to_sql('companies', con=engine, if_exists='replace', index=False)
                                                     
   

if __name__ == '__main__':
    treat_companies()