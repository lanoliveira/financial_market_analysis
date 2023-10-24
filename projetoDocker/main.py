from get_codigo import get_codigo
from get_actions_data import get_actions_data
from read_html_investidor10 import read_html
from treat_companies import treat_companies


def main():
    get_codigo()
    get_actions_data()
    read_html()
    treat_companies()

if __name__ == '__main__':
    main()