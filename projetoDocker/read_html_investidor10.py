import os
import pandas as pd
from lxml import etree
from bs4 import BeautifulSoup


def get_content(dom, path, filename):
    try:
        return dom.xpath (path)[0].text
    except:
        return None


def read_html():
    path = './data/html'

    companies = []

    for filename in os.scandir(path):

        # open txt file
        with open(filename.path, encoding='utf-8') as file:

            html = file.read()
            html = " ".join(html.split()).replace('> <', '><')
            soup = BeautifulSoup(html, 'html.parser')
            dom = etree.HTML (str(soup))

            
            
            company= {}

            company['codigo'] = dom.xpath('//*[@id="header_action"]/div[1]/div[2]/h1')[0].text

            company['empresa'] = soup.find('h2', class_='name-company').text

            company['cotacao'] = get_content(dom, '//*[@id="cards-ticker"]/div[1]/div[2]/div/span', filename)
            
            company['rent_mes'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[2]/span', filename)
        
            company['rent_3_meses'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[3]/span', filename)
        
            company['rent_1_ano'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[4]/span', filename)
        
            company['rent_2_anos'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[5]/span', filename)
        
            company['rent_5_anos'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[6]/span', filename)

            company['rent_10_anos'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[7]/span', filename)

            company['rent_real_mes'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[9]/span', filename)

            company['rent_real_3_meses'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[10]/span', filename)

            company['rent_real_1_ano'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[11]/span', filename)

            company['rent_real_2_anos'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[12]/span', filename)

            company['rent_real_5_anos'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[13]/span', filename)

            company['rent_real_10_anos'] = get_content(dom, '//*[@id="ticker"]/section/div/div[2]/div/div/div[14]/span', filename)

            company['p/l'] = get_content(dom, '//*[@id="cards-ticker"]/div[3]/div[2]/span', filename)

            company['p/vp'] = get_content(dom, '//*[@id="cards-ticker"]/div[4]/div[2]/span', filename)

            company['divida_liquida/ebitda'] = get_content(dom, '//*[@id="table-indicators"]/div[24]/div[1]/span', filename)

            company['divida_liquida/patrimonio'] = get_content(dom, '//*[@id="table-indicators"]/div[23]/div[1]/span', filename)
            
            company['ev/ebitda'] = get_content(dom, '//*[@id="table-indicators"]/div[10]/div[1]/span', filename)

            company['ev/ebit'] = get_content(dom, '//*[@id="table-indicators"]/div[11]/div[1]/span', filename)

            company['p/ebitda'] = get_content(dom, '//*[@id="table-indicators"]/div[12]/div[1]/span', filename)

            company['p/ebit'] = get_content(dom, '//*[@id="table-indicators"]/div[13]/div[1]/span', filename)

            company['margem_ebitda'] = get_content(dom, '//*[@id="table-indicators"]/div[9]/div[1]/span', filename)

            company['divida_liquida/ebit'] = get_content(dom, '//*[@id="table-indicators"]/div[25]/div[1]/span', filename)

            company['divida_bruta/patrimonio'] = get_content(dom, '//*[@id="table-indicators"]/div[26]/div[1]/span', filename)

            company['dividend_yield'] = get_content(dom, '//*[@id="table-indicators"]/div[4]/div[1]/span', filename)

            company['payout'] = get_content(dom, '//*[@id="table-indicators"]/div[5]/div[1]/span', filename)

            company['margem_liquida'] = get_content(dom, '//*[@id="table-indicators"]/div[6]/div[1]/span', filename)

            company['margem_bruta'] = get_content(dom, '//*[@id="table-indicators"]/div[7]/div[1]/span', filename)
            
            company['margem_ebit'] = get_content(dom, '//*[@id="table-indicators"]/div[8]/div[1]/span', filename)

            company['roe'] = get_content(dom, '//*[@id="table-indicators"]/div[20]/div[1]/span', filename)
                
            company['roic'] = get_content(dom, '//*[@id="table-indicators"]/div[21]/div[1]/span', filename)

            company['roa'] = get_content(dom, '//*[@id="table-indicators"]/div[22]/div[1]/span', filename)

            company['cagr_receitas_5_anos'] = get_content(dom, '//*[@id="table-indicators"]/div[30]/div[1]/span', filename)

            company['cagr_lucros_5_anos'] = get_content(dom, '//*[@id="table-indicators"]/div[31]/div[1]/span', filename)
        
            company['valor_mercado'] = get_content(dom, '//*[@id="table-indicators-company"]/div[1]/span[2]/div[2]', filename)

            company['valor_firma'] = get_content(dom, '//*[@id="table-indicators-company"]/div[2]/span[2]/div[2]', filename)

            company['patrimorio_liquido'] = get_content(dom, '//*[@id="table-indicators-company"]/div[3]/span[2]/div[2]', filename)

            company['total_papeis'] = get_content(dom, '//*[@id="table-indicators-company"]/div[4]/span[2]/div[2]', filename)

            try:
                company['divida_bruta'] = soup.find('span', string='Dívida Bruta').findNext().find_all('div')[1].text
            except:
                company['divida_bruta'] = None

            try:
                company['divida_liquida'] = soup.find('span', string='Dívida Líquida').findNext().find_all('div')[1].text
            except:
                company['divida_liquida'] = None
                
            company['disponibilidades'] = soup.find('span', string='Disponibilidade').findNextSibling().find_all('div')[1].text

            company['segmento_listagem'] = soup.find('span', string='Segmento de Listagem').findNextSibling().text

            company['liquidez_media_diaria'] = soup.find('span', string='Liquidez Média Diária').findNextSibling().find_all('div')[1].text

            company['setor'] = soup.find('span', string='Setor').findNextSibling().text

            company['segmento'] = soup.find('span', string='Segmento').findNextSibling().text

            company['sobre'] = soup.find('div', class_='text-content').text.split('História ')[0].strip()

            company['informacoes_complementares'] = soup.find('div', class_='text-content').text.split('Informações Complementares')[1].strip()

            companies.append(company)

            
    df = pd.DataFrame(companies)
    df.to_csv('./data/csv/companies.csv', index=False, sep=';', encoding='utf-8')

if __name__ == "__main__":
    read_html()