import requests
from urllib.parse import urljoin
from parsers.news_item_parser import NewsItemParser
from models.news_item import NewsItem
from models.news_website import NewsWebsite


class NewsScanner:
    def __init__(self, news_website: NewsWebsite, news_item_parser: NewsItemParser):
        """Scans a news website front page for news items

        :param news_website: NewsWebsite describing news website to scan
        :param news_item_parser: NewsItemParser to use to parse the news website front page
        """
        self.news_website = news_website
        self.news_item_parser = news_item_parser

    def _get_web_page_content(self):
        r = requests.get(self.news_website.front_page_url, timeout=5)
        return r.content

    def get_news_items(self) -> [NewsItem]:
        """Scans the website front page, returns a list of parsed NewsItems with transformations performed

        Transformations performed are for each news item so that the URL becomes a full/absolute URL.

        :return: [NewsItem]
        """
        news_items = self.news_item_parser.get_news_items(self._get_web_page_content())
        for item in news_items:
            item.url = urljoin(self.news_website.base_url, item.url)
        return news_items
