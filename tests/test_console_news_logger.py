import unittest
import unittest.mock
import io
from datetime import datetime
from loggers.console_news_logger import ConsoleNewsLogger
from models.news_item import NewsItem
from models.news_website import NewsWebsite


class TestConsoleNewsLogging(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_news_scan_starting(self, mock_stdout):
        timestamp = datetime.now()
        ConsoleNewsLogger().log_news_scan_starting(timestamp)
        expected = "<<<<<<<<<<>>>>>>>>>>\n"
        expected += "Starting news scan at: {}\n".format(timestamp)
        expected += "<<<<<<<<<<>>>>>>>>>>\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_news_scan_ending(self, mock_stdout):
        timestamp = datetime.now()
        ConsoleNewsLogger().log_news_scan_ending(timestamp)
        expected = "<<<<<<<<<<>>>>>>>>>>\n"
        expected += "Ending news scan at: {}\n".format(timestamp)
        expected += "<<<<<<<<<<>>>>>>>>>>\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_news_item_added(self, mock_stdout):
        news_website = NewsWebsite('ABC News', "www.abc.com", "www.abc.com/news")
        news_item = NewsItem("www.abc.com/news/a-story", "A Story", None, None, None, news_website)
        ConsoleNewsLogger().log_news_item_added(news_item)
        expected = "\n===============\n"
        expected += "News item added\n"
        expected += "---------------\n"
        expected += "Time: {}\n".format(news_item.created_at)
        expected += "Website: ABC News\n"
        expected += "URL: www.abc.com/news/a-story\n"
        expected += "Title: A Story\n"
        expected += "===============\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_news_item_added_with_topic(self, mock_stdout):
        news_website = NewsWebsite('ABC News', "www.abc.com", "www.abc.com/news")
        news_item = NewsItem("www.abc.com/news/a-story", "A Story", None, None, 'Australia', news_website)
        ConsoleNewsLogger().log_news_item_added(news_item)
        expected = "\n===============\n"
        expected += "News item added\n"
        expected += "---------------\n"
        expected += "Time: {}\n".format(news_item.created_at)
        expected += "Website: ABC News\n"
        expected += "URL: www.abc.com/news/a-story\n"
        expected += "Title: A Story\n"
        expected += "Topic: Australia\n"
        expected += "===============\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_news_item_added_with_author(self, mock_stdout):
        news_website = NewsWebsite('ABC News', "www.abc.com", "www.abc.com/news")
        news_item = NewsItem("www.abc.com/news/a-story", "A Story", None, 'John Smith', None, news_website)
        ConsoleNewsLogger().log_news_item_added(news_item)
        expected = "\n===============\n"
        expected += "News item added\n"
        expected += "---------------\n"
        expected += "Time: {}\n".format(news_item.created_at)
        expected += "Website: ABC News\n"
        expected += "URL: www.abc.com/news/a-story\n"
        expected += "Title: A Story\n"
        expected += "Author: John Smith\n"
        expected += "===============\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_news_item_added_with_content(self, mock_stdout):
        news_website = NewsWebsite('ABC News', "www.abc.com", "www.abc.com/news")
        news_item = NewsItem("www.abc.com/news/a-story", "A Story", "This is a story summary.", None, None, news_website)
        ConsoleNewsLogger().log_news_item_added(news_item)
        expected = "\n===============\n"
        expected += "News item added\n"
        expected += "---------------\n"
        expected += "Time: {}\n".format(news_item.created_at)
        expected += "Website: ABC News\n"
        expected += "URL: www.abc.com/news/a-story\n"
        expected += "Title: A Story\n"
        expected += "Content: This is a story summary.\n"
        expected += "===============\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_news_item_updated_with_title(self, mock_stdout):
        news_website = NewsWebsite('ABC News', "www.abc.com", "www.abc.com/news")
        news_item = NewsItem("www.abc.com/news/a-story", "An Updated Story", None, None, None, news_website)
        ConsoleNewsLogger().log_news_item_updated(news_item, {'title': 'A Story'})
        expected = "\n===============\n"
        expected += "Existing news item updated\n"
        expected += "---------------\n"
        expected += "Time: {}\n".format(news_item.updated_at)
        expected += "Website: ABC News\n"
        expected += "URL: www.abc.com/news/a-story\n"
        expected += "Title: An Updated Story\n"
        expected += "---------------\n"
        expected += 'Title changed from: "A Story" to: "An Updated Story"\n'
        expected += "===============\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_news_item_updated_with_topic(self, mock_stdout):
        news_website = NewsWebsite('ABC News', "www.abc.com", "www.abc.com/news")
        news_item = NewsItem("www.abc.com/news/a-story", "A Story", None, None, 'Australia', news_website)
        ConsoleNewsLogger().log_news_item_updated(news_item, {'topic': None})
        expected = "\n===============\n"
        expected += "Existing news item updated\n"
        expected += "---------------\n"
        expected += "Time: {}\n".format(news_item.updated_at)
        expected += "Website: ABC News\n"
        expected += "URL: www.abc.com/news/a-story\n"
        expected += "Title: A Story\n"
        expected += "Topic: Australia\n"
        expected += "---------------\n"
        expected += 'Topic changed from: "None" to: "Australia"\n'
        expected += "===============\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_news_item_updated_with_author(self, mock_stdout):
        news_website = NewsWebsite('ABC News', "www.abc.com", "www.abc.com/news")
        news_item = NewsItem("www.abc.com/news/a-story", "A Story", None, 'John Smith', None, news_website)
        ConsoleNewsLogger().log_news_item_updated(news_item, {'author': None})
        expected = "\n===============\n"
        expected += "Existing news item updated\n"
        expected += "---------------\n"
        expected += "Time: {}\n".format(news_item.updated_at)
        expected += "Website: ABC News\n"
        expected += "URL: www.abc.com/news/a-story\n"
        expected += "Title: A Story\n"
        expected += "Author: John Smith\n"
        expected += "---------------\n"
        expected += 'Author changed from: "None" to: "John Smith"\n'
        expected += "===============\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_news_item_updated_with_content(self, mock_stdout):
        news_website = NewsWebsite('ABC News', "www.abc.com", "www.abc.com/news")
        news_item = NewsItem("www.abc.com/news/a-story", "A Story", "This is a story summary.", None, None, news_website)
        ConsoleNewsLogger().log_news_item_updated(news_item, {'content': None})
        expected = "\n===============\n"
        expected += "Existing news item updated\n"
        expected += "---------------\n"
        expected += "Time: {}\n".format(news_item.updated_at)
        expected += "Website: ABC News\n"
        expected += "URL: www.abc.com/news/a-story\n"
        expected += "Title: A Story\n"
        expected += "Content: This is a story summary.\n"
        expected += "---------------\n"
        expected += 'Content changed from: "None" to: "This is a story summary."\n'
        expected += "===============\n"
        self.assertEqual(expected, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
