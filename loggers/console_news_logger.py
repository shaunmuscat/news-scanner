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
        if news_item.content is not None:
            print("Content: {}".format(news_item.content))
        if news_item.author is not None:
            print("Author: {}".format(news_item.author))
        if news_item.topic is not None:
            print("Topic: {}".format(news_item.topic))
        print("===============")

    @staticmethod
    def __print_changed_value(attr_display_name, old_value, new_value):
        print('{} changed from: "{}" to: "{}"'.format(attr_display_name, old_value, new_value))

    def log_news_item_updated(self, news_item: NewsItem, original_values: dict):
        print("\n===============")
        print("Existing news item updated")
        print("---------------")
        print("Time: {}".format(news_item.updated_at))
        print("Website: {}".format(news_item.news_website.name))
        print("URL: {}".format(news_item.url))
        print("Title: {}".format(news_item.title))
        if 'content' in original_values:
            print("Content: {}".format(news_item.content))
        if 'author' in original_values:
            print("Author: {}".format(news_item.author))
        if 'topic' in original_values:
            print("Topic: {}".format(news_item.topic))
        print("---------------")
        if 'title' in original_values:
            self.__print_changed_value('Title', original_values.get('title'), news_item.title)
        if 'content' in original_values:
            self.__print_changed_value('Content', original_values.get('Content'), news_item.content)
        if 'author' in original_values:
            self.__print_changed_value('Author', original_values.get('Author'), news_item.author)
        if 'topic' in original_values:
            self.__print_changed_value('Topic', original_values.get('topic'), news_item.topic)
        print("===============")
