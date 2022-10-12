from enum import Enum
from typing import List, Union
from typing import Dict

from finnews.parser import NewsParser
from finnews.fields import googleNews_rss_url_id
from finnews.fields import googleNews_rss_local_id
from finnews.fields import googleNews_rss_time_id


class GGNews():

    def __init__(self):
        self.url = 'https://news.google.com/rss/search?q=when:{time_id}+site:{url_id}&ceid={local_id}'

        self.time_categories: dict = googleNews_rss_time_id
        self.url_categories: dict = googleNews_rss_url_id
        self.local_categories: dict = googleNews_rss_local_id
        
        self.news_parser = NewsParser(client='ggnews')

    def __repr__(self):
        
        return "<Google news Connected: True'>"
    #Kiểm tra giá trị nhập vào có trong fields.py hay không
    def _check(self, time_id: str,url_id: str,local_id: str):
        if time_id in self.time_categories:
            if url_id in self.url_categories:
                if local_id in self.local_categories:
                    full_url = self.url.format(
                        time_id=self.time_categories[time_id],
                        url_id=self.url_categories[url_id],
                        local_id=self.local_categories[local_id]
                    )
                    return full_url
                else:
                    raise KeyError("The value you're searching for does not exist.")
            else:
                raise KeyError("The value you're searching for does not exist.")
        else:
            raise KeyError("The value you're searching for does not exist.")
    # lấy tất cả news 
    def news(self):
        print(self._check('','',''))
        data = self.news_parser._make_request(
            url=self._check('','','')
        )
        return data
    # lấy news trong những trang định sẵn
    def getnews(self, time: Union[str, Enum],url: Union[str, Enum],local: Union[str, Enum]):

        if isinstance(time, Enum):
            time = time.name.lower()
        if isinstance(url, Enum):
            url = url.name.lower()
        if isinstance(local, Enum):
            local = local.name.lower()
        print(self._check(time,url,local))
        data = self.news_parser._make_request(
            url=self._check(time,url,local)
        )
        return data
    # lấy news bằng url không an toàn 
    # Có thể gây ra lỗi
    def getnewsinsecure(self,time:str, url:str,local: str):
        try:
            data = self.news_parser._make_request(
                url=self.url.format(
                    time_id=time,
                    url_id=url,
                    local_id=local
                )
            )
            return data
        except:
            return False
        
