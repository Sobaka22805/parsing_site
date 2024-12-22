from bs4 import BeautifulSoup
import requests

site = requests.get('https://bank.gov.ua/')

if site.status_code == 200:

    item_site = BeautifulSoup(site.text, features='html.parser')
    # exchange_rate = item_site.find_all('div', {'class', 'collection-item indicator with-dir'})
    dollar = item_site.find_all('div', {'class', 'left'})

    for exchange in dollar:
        # 4-я строка, это доллар
        test = exchange.findNext().text[125:]
        print(test)

# я не смог сделать конвертер валют, извините