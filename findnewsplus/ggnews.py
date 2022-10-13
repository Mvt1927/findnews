from distutils.log import debug
from enum import Enum
from tabnanny import check
from typing import List, Union
from typing import Dict

from finnews.parser import NewsParser
from finnews.fields import googleNews_rss_url_id
from finnews.fields import googleNews_rss_local_id
from finnews.fields import googleNews_rss_time_id


class GGNews():

    def __init__(self):
        self.url = 'https://news.google.com/rss/search?q={url_id}{time_id}{local_id}'
        self.url_topic = 'https://news.google.com/rss/search?q={topic_id}%20{url_id}{time_id}{local_id}'
        
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
                        time_id="+when:"+self.time_categories[time_id],
                        url_id="site:"+self.url_categories[url_id],
                        local_id="&ceid="+self.local_categories[local_id]
                    )
                    return full_url
                else:
                    raise KeyError("The value you're searching for does not exist.")
            else:
                raise KeyError("The value you're searching for does not exist.")
        else:
            raise KeyError("The value you're searching for does not exist.")
    def _checkTopic(self,topic_id:str, time_id: str,url_id: str,local_id: str):
        if time_id in self.time_categories:
            if url_id in self.url_categories:
                if local_id in self.local_categories:
                    full_url = self.url_topic.format(
                        topic_id = topic_id,
                        time_id="+when:"+self.time_categories[time_id],
                        url_id="site:"+self.url_categories[url_id],
                        local_id="&ceid="+self.local_categories[local_id]
                    )
                    print("DEBUG: "+full_url)
                    return full_url
                else:
                    raise KeyError("The value you're searching for does not exist.")
            else:
                raise KeyError("The value you're searching for does not exist.")
        else:
            raise KeyError("The value you're searching for does not exist.")
    def _checkListUrl(self, time_id: str,listUrls: List[str],local_id: str):
        if time_id in self.time_categories:
            urls_id = ''
            check = True;
            for url_id in listUrls:
                if url_id in self.url_categories:
                    urls_id += " OR site:" + self.url_categories[url_id]  
                else:
                    check = False
                    raise KeyError("The value you're searching for does not exist.")
            if check:
                urls_id = urls_id.replace(" OR ", '', 1)
                if local_id in self.local_categories:
                    full_url = self.url.format(
                        time_id="+when:"+self.time_categories[time_id],
                        url_id=urls_id,
                        local_id="&ceid="+self.local_categories[local_id]
                    )
                    return full_url
                else:
                    raise KeyError("The value you're searching for does not exist.")
            else:
                raise KeyError("The value you're searching for does not exist.")
        else:
            raise KeyError("The value you're searching for does not exist.")
    # lấy tất cả news 
    def _checkTopicListUrl(self,topic:str, time_id: str,listUrls: List[str],local_id: str):
        if time_id in self.time_categories:
            urls_id = ''
            check = True;
            for url_id in listUrls:
                if url_id in self.url_categories:
                    urls_id += " OR site:" + self.url_categories[url_id]  
                else:
                    check = False
                    raise KeyError("The value you're searching for does not exist.")
            if check:
                urls_id = urls_id.replace(" OR ", '', 1)
                if local_id in self.local_categories:
                    full_url = self.url.format(
                        topic_id=topic,
                        time_id="+when:"+self.time_categories[time_id],
                        url_id=urls_id,
                        local_id="&ceid="+self.local_categories[local_id]
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
        # print(self._check('','',''))
        data = self.news_parser._make_request(
            url="https://news.google.com/rss?cf=all"   
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
        # print(self._check(time,url,local))
        data = self.news_parser._make_request(
            url=self._check(time,url,local)
        )
        return data
    def getnewsTopic(self,topic:str, time: Union[str, Enum],url: Union[str, Enum],local: Union[str, Enum]):
        if isinstance(time, Enum):
            time = time.name.lower()
        if isinstance(url, Enum):
            url = url.name.lower()
        if isinstance(local, Enum):
            local = local.name.lower()
        # print(self._check(time,url,local))
        data = self.news_parser._make_request(
            url=self._checkTopic(topic,time,url,local)
        )
        return data
    
    def getnewsList(self, time: Union[str, Enum],urls: List[Union[str, Enum]],local: Union[str, Enum]):
    
        if isinstance(time, Enum):
            time = time.name.lower()
        listUrl = []
        for url in urls:
            if isinstance(url, Enum):
                listUrl.append(url.name.lower())
            else:
                listUrl.append(url.lower())
        if isinstance(local, Enum):
            local = local.name.lower()
        # print(self._checkListUrl(time,listUrl,local))
        data = self.news_parser._make_request(
            url=self._checkListUrl(time,listUrl,local)
        )
        return data
    def getnewsTopicList(self,topic:str, time: Union[str, Enum],urls: List[Union[str, Enum]],local: Union[str, Enum]):

        if isinstance(time, Enum):
            time = time.name.lower()
        listUrl = []
        for url in urls:
            if isinstance(url, Enum):
                listUrl.append(url.name.lower())
            else:
                listUrl.append(url.lower())
        if isinstance(local, Enum):
            local = local.name.lower()
        # print(self._checkListUrl(time,listUrl,local))
        data = self.news_parser._make_request(
            url=self._checkTopicListUrl(topic,time,listUrl,local)
        )
        return data
    
    # lấy news bằng url không an toàn 
    # Có thể gây ra lỗi
    def getnewsinsecure(self,time:str, url:str,local: str):
        try:
            data = self.news_parser._make_request(
                url=self.url.format(
                    time_id="+when:"+time,
                    url_id="site:"+url,
                    local_id="&ceid="+local
                )
            )
            return data
        except:
            return False
    def getnewsTopicInsecure(self,topic:str,time:str, url:str,local: str):
        try:
            if time!='':
                time = "+when:"+time
            if local!='':
                local = "&ceid="+local
            data = self.news_parser._make_request(
                url=self.url_topic.format(
                    topic_id=topic,
                    time_id=time,
                    url_id="site:"+url,
                    local_id=local
                )
            )
            return data
        except:
            return False
        
    def getnewsListInsecure(self, time:str,urls: List[str],local:str):
        try:
            if time!='':
                time = "+when:"+time
            if local!='':
                local = "&ceid="+local
            fullUrl = ''
            for url in urls:
                fullUrl += " OR site:"+ url.lower()
            fullUrl = fullUrl.replace(" OR ",'',1)
            data = self.news_parser._make_request(
                url=self.url.format(
                    time_id=time,
                    url_id=fullUrl,
                    local_id=local
                )
            )
            return data
        except :
            return False
    def getnewsTopicListInsecure(self,topic:str, time:str,urls: List[str],local:str):
        try:
            if time!='':
                time = "+when:"+time
            if local!='':
                local = "&ceid="+local
            fullUrl = ''
            for url in urls:
                fullUrl += " OR site:"+ url.lower()
            fullUrl = fullUrl.replace(" OR ",'',1)
            data = self.news_parser._make_request(
                url=self.url_topic.format(
                    topic_id=topic,
                    time_id=time,
                    url_id=fullUrl,
                    local_id=local
                )
            )
            return data
        except :
            return False
