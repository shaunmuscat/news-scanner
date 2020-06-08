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
        expected = "--------------\n"
        expected += "News item added\n"
        expected += "Time: {}\n".format(news_item.created_at)
        expected += "Website: ABC News\n"
        expected += "URL: www.abc.com/news/a-story\n"
        expected += "Title: A Story\n"
        expected += "--------------\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_news_item_updated(self, mock_stdout):
        news_website = NewsWebsite('ABC News', "www.abc.com", "www.abc.com/news")
        news_item = NewsItem("www.abc.com/news/a-story", "An Updated Story", None, None, None, news_website)
        ConsoleNewsLogger().log_news_item_updated(news_item, {'title': 'A Story'})
        expected = "--------------\n"
        expected += 'title changed from: "A Story" to: "An Updated Story"\n'
        expected += "--------------\n"
        expected += "Existing news item updated\n"
        expected += "Time: {}\n".format(news_item.updated_at)
        expected += "Website: ABC News\n"
        expected += "URL: www.abc.com/news/a-story\n"
        expected += "Title: An Updated Story\n"
        expected += "--------------\n"
        self.assertEqual(expected, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()