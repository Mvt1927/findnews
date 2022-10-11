from enum import Enum
from typing import List, Union
from typing import Dict

from finnews.parser import NewsParser
from finnews.fields import ft_rss_id


class FT():

    def __init__(self):
        self.url = 'https://www.ft.com/{topic_id}?format=rss'

        self.topic_categories: dict = ft_rss_id
        
        self.news_parser = NewsParser(client='pt')

    def __repr__(self):
        
        return "<Financial Times Connected: True'>"
    
    def _check_key(self, topic_id: str):
        if topic_id in self.topic_categories:

            full_url = self.url.format(
                topic_id=self.topic_categories[topic_id]
            )
            return full_url
        else:
            raise KeyError("The value you're searching for does not exist.")
        
    def news(self):
        
        data = self.news_parser._make_request(
            url=self._check_key(topic_id='home')
        )
        return data
    
    def getnews(self, topic: Union[str, Enum]):

        if isinstance(topic, Enum):
            topic = topic.name.lower()
        print(self._check_key(topic_id=topic))
        data = self.news_parser._make_request(
            url=self._check_key(topic_id=topic)
        )

        return data
    def headlines(self, symbols: List[str]):
        params = {
            's': ','.join(symbols),
            'region': 'US',
            'lang': 'en-US'
        }
        data = self.news_parser._make_request(
            url=self._check_key(topic_id="home"),
            params=params
        )
        return data
