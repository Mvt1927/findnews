from cgi import test
import json
from pprint import pprint
import pandas as pd

from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the Google News Client.
google_news_client = news_client.ggnews

# Grab the news form url.
# news = google_news_client.getnewsList(time='1h',urls=['business-standard.com','ft.com'],local='US:en')
# news = google_news_client.getnewsListInsecure(time='',urls=['https://vtc.vn/','https://vnexpress.net/'],local='VN:vi')
# news = google_news_client.getnewsTopic(topic='Suc khoe', time='',urls=['https://vtc.vn/','https://vnexpress.net/'],local='VN:vi')
# news = google_news_client.getnewsTopic(topic='Suc khoe', time='',url='https://vtc.vn/',local='VN:vi')
news = google_news_client.getnewsTopicListInsecure(topic='Suc khoe', time='',urls=['https://vtc.vn/'],local='VN:vi')

# Print it.
pprint(news)

# Print to excel
data_json = json.dumps(news)
df_json = pd.read_json(data_json)
df_json.to_excel('responses/test.xlsx')
