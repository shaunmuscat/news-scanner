import unittest
from tests.helpers import get_test_data_file_contents
from parsers.sbs_news_item_parser import SbsNewsItemParser


class TestSbsNewsItemParser(unittest.TestCase):
    def test_get_news_items(self):
        parser = SbsNewsItemParser()
        news_items = parser.get_news_items(get_test_data_file_contents("sbs_news.html"))
        self.assertEqual(len(news_items), 53)

        # Test first news item
        self.assertEqual("/news/two-men-charged-after-sydney-anti-racism-protests", news_items[0].url)
        self.assertEqual("Two men charged after Sydney anti-racism protests", news_items[0].title)
        self.assertEqual("Australia", news_items[0].topic)

        # Test last news item
        self.assertEqual("There are fears coronavirus is stopping Australia's migrant women from accessing abortions",
                         news_items[-1].title)
        self.assertEqual("/news/there-are-fears-coronavirus-is-stopping-australia-s-migrant-women-from-accessing-abortions",
                         news_items[-1].url)
        self.assertEqual(None, news_items[-1].topic)


if __name__ == '__main__':
    unittest.main()
