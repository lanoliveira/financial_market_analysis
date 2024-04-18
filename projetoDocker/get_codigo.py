import pandas as pd
import os

def createFolders():
    if not os.path.exists('./data/csv'):
        os.makedirs('./data/csv')

def get_codigo():
    df = pd.read_html('https://www.dadosdemercado.com.br/bolsa/acoes')[0]

    dfActions = df[['Nome', 'Ticker']].copy()
    dfActions['Nome'] = dfActions['Nome'].str.lower()
    dfActions['codigo'] = dfActions['Ticker'].str.lower()


    dfActions.to_csv('./data/csv/actions_title_code.csv', sep=';', index=False)

if __name__ == '__main__':
    createFolders()
    get_codigo()