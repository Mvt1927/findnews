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
news = google_news_client.getnews(time='1d',url='business-standard.com',local='US:en')

# Print it.
pprint(news)

# Print to excel
data_json = json.dumps(news)
df_json = pd.read_json(data_json)
df_json.to_excel('responses/business-standard.com.xlsx')
