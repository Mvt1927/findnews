from enum import Enum
from typing import List, Union
from typing import Dict

from finnews.parser import NewsParser


class Bloomberg():

    def __init__(self):
        self.url = 'https://www.newslookup.com/rss/business/bloomberg.rss'
        
        self.news_parser = NewsParser(client='bloomberg')

    def __repr__(self):
        
        return "<Financial Times Connected: True'>"
    
    def getnews(self):
        data = self.news_parser._make_request(
            url=self.url
        )
        return data
    def headlines(self, symbols: List[str]):
        params = {
            's': ','.join(symbols),
            'region': 'US',
            'lang': 'en-US'
        }
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )
        return data
