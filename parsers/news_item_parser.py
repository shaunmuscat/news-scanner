from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from models.news_item import NewsItem


class NewsItemParser(ABC):
    def __init__(self):
        """ Abstract base class to parse news items matching a specific HTML element structure
        """
        super().__init__()

    @staticmethod
    def _get_page_soup(html):
        return BeautifulSoup(html, 'html.parser')

    @abstractmethod
    def get_news_items(self, html) -> [NewsItem]:
        """Gets all news items within the given HTML

        :param html: news page HTML
        :return: list of NewsItem
        """
