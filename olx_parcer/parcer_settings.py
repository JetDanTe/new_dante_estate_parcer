g_url_to_parse = 'https://www.olx.ua/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/'
# url with all queries = https://www.olx.ua/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/1-komnata/odessa/?search%5Bfilter_float_price%3Afrom%5D=5000&search%5Bfilter_float_price%3Ato%5D=10000&search%5Bfilter_enum_cooperate%5D%5B0%5D=1&search%5Bfilter_float_floor%3Afrom%5D=1&search%5Bfilter_float_floor%3Ato%5D=11&search%5Bfilter_float_total_floors%3Afrom%5D=1&search%5Bfilter_float_total_floors%3Ato%5D=20&search%5Bfilter_float_total_area%3Afrom%5D=20&search%5Bfilter_float_total_area%3Ato%5D=50&search%5Bfilter_float_kitchen_area%3Afrom%5D=5&search%5Bfilter_float_kitchen_area%3Ato%5D=25


import parcer_settings
import requests, time
from bs4 import BeautifulSoup

