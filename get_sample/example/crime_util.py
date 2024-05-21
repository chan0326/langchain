from abc import ABCMeta, abstractmethod
import json
import os
from dotenv import load_dotenv
import pandas as pd
from example.crime_abstract import ScraperBase, printerBase , EditorBase
import googlemaps
from selenium import webdriver
from icecream import ic
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
load_dotenv(os.path.join(BASE_DIR, '.env'))


class EditorBase(EditorBase):
    def dropna(self, this: pd.DataFrame) -> pd.DataFrame:
        this.dropna()



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

    def csv(self, file) -> pd.DataFrame:
        return pd.read_csv(f'{file}.csv', encoding='utf-8', thousands=',', index_col=None)

    def xls(self, file ,header , usecols) -> pd.DataFrame:
        return pd.read_excel(f'{file}.xls', header=header, usecols=usecols)
    
    def json(self, file: str) -> pd.DataFrame:
        return json.load(open(f'{file}.json', encoding='utf-8'))
    
    def gmaps(self) -> pd.DataFrame:
        return googlemaps.Client(key = os.environ['api_key'])


class Scraper(ScraperBase):

    def __init__(self) -> None:
        pass

    def driver(self) -> object:
        return webdriver.Chrome('C:/Program Files/Google/Chrome/chromedriver.exe')
    
    def auto_login(self, driver, url, selector, data) -> None:
        driver.get(url)
        driver.find_element_by_css_selector(selector).send_keys(data)
        driver.find_element_by_css_selector(selector).submit()
    
