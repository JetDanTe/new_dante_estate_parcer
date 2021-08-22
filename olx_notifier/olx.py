import os
from bs4 import BeautifulSoup
import re

import requests

class OlxApi():
    def __init__(self, filter, last_adv):
        self.filter = filter
        self.__req = requests.session()
        self.last_adv = last_adv

    @property
    def url(self) -> str:
        return f"https://www.olx.ua/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/{self.filter.get('city', 'odessa')}" \
               f"/?search%5Bfilter_float_price%3Afrom%5D={self.filter.get('min_pr', 2000)}&search%5Bfilter_float_" \
               f"price%3Ato%5D={self.filter.get('max_pr', 100000)}"


    def get_adv(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        list_adv = []
        for adv in soup.findAll('td', class_='offer'):
            link = adv.a.attrs['href']
            adv_data = self.detail(link)
            if adv_data['id'] == self.last_adv:
                break
            if len(list_adv) > 11:
                break
            list_adv.append(adv_data)
        return list_adv


    def detail(self, link):
        ret = {'id': 0, 'price': '-', 'title': '-', 'description': '-'}
        regex = r"ID: (\d{2,})"
        description = requests.get(link)
        desc_soup = BeautifulSoup(description.content, 'html.parser')
        ret['title'] = desc_soup.h1.text
        ret['price'] = desc_soup.h3.text
        for elem in desc_soup.findAll('div'):
            if 'data-cy' in elem.attrs and elem.attrs['data-cy'] == 'ad_description':
                ret['description'] = elem.text.replace('Описание', '')
                break
        ret['id'] = re.findall(regex, desc_soup.body.text)
        return ret

