# Get News Aggregator

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)

## Overview

Current Version: **1.0**

Add a few functions, delete old files. The project is further developed from the [Finance News Aggregator](https://github.com/areed1192/finance-news-aggregator) - [areed1192](https://github.com/areed1192) project.
## Setup

To **install** the library, run the following command from the terminal.

```console
pip install fin-news
```

To **upgrade** the library, run the following command from the terminal.

```console
pip install --upgrade fin-news
```

## Usage

Here is a simple example of using the `finnews` library to to grab the news.

```python
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
```

