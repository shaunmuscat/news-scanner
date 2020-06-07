import requests
import datetime
from news_item_parser import NewsItemParser


class NewsScanner:
    def __init__(self, website_name: str, url: str, news_parser: NewsItemParser):
        self.website_name = website_name
        self.url = url
        self.news_item_parser = news_parser

    def get_web_page_content(self):
        r = requests.get(self.url, timeout=5)
        return r.content

    def get_news_items(self):
        items = self.news_item_parser.find_news_items(self.get_web_page_content())
        scanned_items = []
        for item in items:
            scanned_items.append({
                'time': datetime.datetime.now(),
                'website name': self.website_name,
                'url': self.news_item_parser.get_item_url(item),
                'content': self.news_item_parser.get_item_title(item)
            })
        return scanned_items


if __name__ == "__main__":
    news_scanners = {
        "sbs": NewsScanner("SBS News", "https://www.sbs.com.au/news/",
                           NewsItemParser('div', 'preview__wrap', None, 'headline', 'a', None)),
        "abc": NewsScanner("ABC News", "https://www.abc.net.au/news/",
                           NewsItemParser(None, 'doctype-article','h3', None, 'a', None)),
        "nine": NewsScanner("Nine News", "https://www.9news.com.au/",
                            NewsItemParser('article', 'story-block', 'h3', 'story__headline', 'a', 'story__link')),
        "australian": NewsScanner("The Australian", "https://www.theaustralian.com.au/",
                                  NewsItemParser('div', 'story-block', 'h3', 'story-block__heading', 'a', None))
    }

    for k, scanner in news_scanners.items():
        for item in scanner.get_news_items():
            print("--------------")
            # ToDo: add db to differentiate between new and updated news items
            print("New item added")
            print("Time: {}".format(item.get('time')))
            print("Website: {}".format(item.get('website name')))
            # ToDo: add check to add base to url if not fully qualified
            print("URL: {}".format(item.get('url')))
            print("Content: {}".format(item.get('content')))
            print("--------------")

