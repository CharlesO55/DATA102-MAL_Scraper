import requests

from bs4 import BeautifulSoup

import time
import numpy as np

from enum import Enum

class Scraper:
    MINIMUM_DELAY : int = 5
    
    class SEASONS(Enum):
        FALL = 'fall'
        SPRING = 'spring'
        SUMMER = 'summer'
        WINTER = 'winter'
    
    @staticmethod
    def build_URL_Seasons(year : str | int, 
                          season : SEASONS) -> str:

        return f"https://myanimelist.net/anime/season/{year}/{season.value}"

    @staticmethod
    def delay():
        time.sleep(np.random.rand() * 10 + Scraper.MINIMUM_DELAY)

    @staticmethod
    def scrape(url : str) -> BeautifulSoup:
        #include a delay per get() to avoid DDOS 
        Scraper.delay()
        
        response = requests.get(url)
        if response.status_code != requests.status_codes.codes.all_ok:
            raise ConnectionError
        
        return BeautifulSoup(response.text, 'html.parser')