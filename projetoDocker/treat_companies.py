import pandas as pd
from sqlalchemy import create_engine

def treat_companies():
    # dialect+driver://username:password@host:port/database
    engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres/postgres")

    data = pd.read_csv('./data/csv/companies.csv', sep=';', encoding='utf-8')

    def treat(data):
        if isinstance(data, str):
            data = data.strip()
            data = data.replace('R$', '').replace('%', '').replace('.', '').replace(',', '.').strip()
            if data == '' or data == '-':
                    return None
        return data

    columns = ['cotacao', 'rent_mes', 'rent_3_meses',
       'rent_1_ano', 'rent_2_anos', 'rent_5_anos', 'rent_10_anos',
       'rent_real_mes', 'rent_real_3_meses', 'rent_real_1_ano',
       'rent_real_2_anos', 'rent_real_5_anos', 'rent_real_10_anos', 'p/l',
       'p/vp', 'divida_liquida/ebitda', 'divida_liquida/patrimonio',
       'ev/ebitda', 'ev/ebit', 'p/ebitda', 'p/ebit', 'margem_ebitda',
       'divida_liquida/ebit', 'divida_bruta/patrimonio', 'dividend_yield',
       'payout', 'margem_liquida', 'margem_bruta', 'margem_ebit', 'roe',
       'roic', 'roa', 'cagr_receitas_5_anos', 'cagr_lucros_5_anos',
       'valor_mercado', 'valor_firma', 'patrimorio_liquido', 'total_papeis',
       'divida_bruta', 'divida_liquida', 'disponibilidades', 'liquidez_media_diaria']
    
    data = data.map(treat)
    
    for column in columns:
        data[column] = data[column].astype(float)

    data.to_sql('companies', con=engine, if_exists='replace', index=False)
             
                                                     
if __name__ == '__main__':
    treat_companies()