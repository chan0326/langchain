import json
import os
from dotenv import load_dotenv
import pandas as pd
from example.crime_abstract import ScraperBase, printerBase
import googlemaps
from selenium import webdriver
from icecream import ic
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
load_dotenv(os.path.join(BASE_DIR, '.env'))

class printer(printerBase):

    def dframe(self, this: pd.DataFrame) -> None:
        print('*'*100)
        ic(f'타입: {type(this)}')
        ic(f'컬럼: {this.columns}')
        ic(f'상위 1개행 {this.head(1)}')
        ic(f'널체크: {this.isnull().sum()}')
        print('*'*100)

class Reader():

    def __init__(self) -> None:
        pass

    def csv(self, file: str) -> object:
        return pd.read_csv(f'{file}', encoding='utf-8', thousands=',')

    def xls(self, file: str,header , usecols) -> object:
        return pd.read_excel(f'{file}', header=header, usecols=usecols)
    
    def json(self, file: str) -> object:
        return json.load(open(f'{file}.json', encoding='utf-8'))
    
    def gmaps(self) -> object:
        return googlemaps.Client(key = os.environ.get('api_key'))


class Scraper(ScraperBase):

    def __init__(self) -> None:
        pass

    def driver(self) -> object:
        return webdriver.Chrome('C:/Program Files/Google/Chrome/chromedriver.exe')
    
    def auto_login(self, driver, url, selector, data) -> None:
        driver.get(url)
        driver.find_element_by_css_selector(selector).send_keys(data)
        driver.find_element_by_css_selector(selector).submit()
    
