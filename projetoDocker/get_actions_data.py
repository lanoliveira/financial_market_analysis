import pandas as pd
import requests
import os
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


def createFolders():
    if not os.path.exists('./data/html'):
        os.makedirs('./data/html')
    

def getSite(url:str, codeCompany:str):
    
    time.sleep(random.uniform(0.3, 0.5))

    r = requests.get(url, headers=headers)

    f = open(f'./data/html/{codeCompany}.html', 'w', encoding='utf-8')
    f.write(r.text)
    f.close()


def get_actions_data():
    
    df = pd.read_csv('./data/csv/actions_title_code.csv', sep=';')

    codeCompanys = df['codigo'].tolist()[0:20]
    
    while len(codeCompanys) > 0:
        codeCompany = codeCompanys.pop()
        url = "https://investidor10.com.br/acoes/" + codeCompany
        time.sleep(random.uniform(0.3, 0.5))    
        getSite(url, codeCompany)


if __name__ == '__main__':
    createFolders()
    get_actions_data()

