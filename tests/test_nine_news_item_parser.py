import unittest
from tests.helpers import get_test_data_file_contents
from parsers.nine_news_item_parser import NineNewsItemParser


class TestNineNewsItemParser(unittest.TestCase):
    def test_get_news_items(self):
        parser = NineNewsItemParser()
        news_items = parser.get_news_items(get_test_data_file_contents("nine_news.html"))

        # Test first news item
        self.assertEqual("https://www.9news.com.au/national/tyaak-house-fire-eleven-hospitalised-two-unaccounted-for/60155f9d-948f-4cc0-a361-14f01bdae415",
                         news_items[0].url)
        self.assertEqual("Two missing after fire rips through home", news_items[0].title)

        # Test last news item
        self.assertEqual("Thousands rally in US capital on 12th day of George Floyd protests",
                         news_items[-1].title)
        self.assertEqual("https://www.9news.com.au/world/george-floyd-protests-thousands-fill-washington-streets/598469e1-2a3e-4b74-8aec-d292c45e7e9c",
                         news_items[-1].url)


if __name__ == '__main__':
    unittest.main()
