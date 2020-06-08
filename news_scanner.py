import requests
from news_item_parser import NewsItemParser
from datetime import datetime
from models.news_website import NewsWebsite


class NewsScanner:
    def __init__(self, news_website: NewsWebsite, news_parser: NewsItemParser):
        """Scans a news website front page for news items

        :param news_website: NewsWebsite describing news website to scan
        :param news_parser: NewsItemParser to use to parse the news website front page
        """
        self.news_website = news_website
        self.news_item_parser = news_parser

    def __get_web_page_content(self):
        r = requests.get(self.news_website.front_page_url, timeout=5)
        return r.content

    def get_news_items(self) -> [dict]:
        """Scans the website front page, parses news items and returns a list of k,v mappings for each news item

        :return: [{'time': `datetime`, 'website_name': `str`, 'url': `str`, 'title': `str`}, ...]
        """
        items = self.news_item_parser.find_news_items(self.__get_web_page_content())
        scanned_items = []
        for item in items:
            scanned_items.append({
                'time': datetime.now(),
                'website_name': self.news_website.name,
                'url': self.news_item_parser.get_item_url(item),
                'title': self.news_item_parser.get_item_title(item)
            })
        return scanned_items
