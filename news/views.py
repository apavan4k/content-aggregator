import feedparser
from django.shortcuts import render

# Create your views here.
def home(request):
    feeds = [
        "https://rss.cnn.com/rss/edition.rss",
        "https://feeds.bbci.co.uk/news/rss.xml",
        "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"

    ]

    all_news = []

    for url in feeds:
        feed = feedparser.parse(url)
        source = feed.feed.get('title','unknown source')

        for entry in feed.entries[:5]:
            all_news.append({
                'source': source,
                'title': entry.title,
                'link': entry.link
            })
    return render(request, "home.html", {"news_list": all_news})