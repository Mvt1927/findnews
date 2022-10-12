from cgi import test
from importlib.resources import path
from pprint import pprint
from findnewsplus.printToXlsx import Print

from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the Google News Client.
google_news_client = news_client.ggnews

url = 'https://www.bloomberg.com/news/articles/2022-10-11/selloff-in-us-listed-china-stocks-worsens-on-covid-growth-fears'

# Grab the news form url.
news = google_news_client.getnewsinsecure(time='',url=url,local='US:en')

# Print it.
pprint(news)

# Print to excel
Print.xlsx(data=news,path="responses/insecure.xlsx")
