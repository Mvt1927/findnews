from pprint import pprint
from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the Google News Client.
google_news_client = news_client.ggnews

# Grab the news form url.
news = google_news_client.getnews(time='1d',url='business-standard.com',local='US:en')

# Print it.
pprint(news)