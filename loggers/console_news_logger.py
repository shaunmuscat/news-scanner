from loggers.news_logger import NewsLogger, NewsItem


class ConsoleNewsLogger(NewsLogger):
    def __init__(self):
        """ Logs news items to console
        """
        super().__init__()

    def log_news_scan_starting(self, timestamp):
        print("<<<<<<<<<<>>>>>>>>>>")
        print("Starting news scan at: {}".format(timestamp))
        print("<<<<<<<<<<>>>>>>>>>>")

    def log_news_scan_ending(self, timestamp):
        print("<<<<<<<<<<>>>>>>>>>>")
        print("Ending news scan at: {}".format(timestamp))
        print("<<<<<<<<<<>>>>>>>>>>")

    def log_news_item_added(self, news_item: NewsItem):
        print("\n===============")
        print("News item added")
        print("---------------")
        print("Time: {}".format(news_item.created_at))
        print("Website: {}".format(news_item.news_website.name))
        print("URL: {}".format(news_item.url))
        print("Title: {}".format(news_item.title))
        print("===============")

    def log_news_item_updated(self, news_item: NewsItem, original_values: dict):
        print('title changed from: "{}" to: "{}"'.format(original_values.get('title'), news_item.title))
        print("\n===============")
        print("Existing news item updated")
        print("---------------")
        print("Time: {}".format(news_item.updated_at))
        print("Website: {}".format(news_item.news_website.name))
        print("URL: {}".format(news_item.url))
        print("Title: {}".format(news_item.title))
        print("---------------")
        print('title changed from: "{}" to: "{}"'.format(original_values.get('title'), news_item.title))
        print("===============")
