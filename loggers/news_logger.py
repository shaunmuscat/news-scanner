from abc import ABC, abstractmethod
from models.news_item import NewsItem


class NewsLogger(ABC):
    def __init__(self):
        """ Abstract base class to logs news items
        """
        super().__init__()

    @abstractmethod
    def log_news_scan_starting(self, timestamp):
        """Logs that a news scan is started at the given timestamp

        :param timestamp: datetime timestamp that the scan is starting at
        :return:
        """

    @abstractmethod
    def log_news_scan_ending(self, timestamp):
        """Logs that a news scan is ending at the given timestamp

       :param timestamp: datetime timestamp that the scan is ending at
       :return:
       """

    @abstractmethod
    def log_news_item_added(self, news_item: NewsItem):
        """Logs that a news item has been added

        :param news_item: NewsItem that was added
        :return:
        """

    @abstractmethod
    def log_news_item_updated(self, news_item: NewsItem, original_values: dict):
        """Logs that an existing news item has been updated

        :param news_item: NewsItem that was updated
        :param original_values: dict containing k - NewsItem field updated, and v - updated NewsItem field original value
        :return:
        """