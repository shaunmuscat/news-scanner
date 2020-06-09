import unittest
from tests.helpers import get_test_data_file_contents
from parsers.the_australian_news_item_parser import TheAustralianNewsItemParser


class TestTheAustralianNewsItemParser(unittest.TestCase):
    def test_get_news_items(self):
        parser = TheAustralianNewsItemParser()
        news_items = parser.get_news_items(get_test_data_file_contents("the_australian.html"))

        # Test first news item
        self.assertEqual("https://www.theaustralian.com.au/nation/coronavirus-australia-live-news-health-officials-fear-second-covid19-spike-after-black-lives-matter-protests/news-story/6ee48b5a626d2391217e59c9ada2c632?keyevent=1.05pm",
                         news_items[0].url)
        self.assertEqual("First new case in ACT in more than a month", news_items[0].title)
        self.assertEqual(None, news_items[0].topic)
        self.assertEqual("Lachlan Moffett-Gray", news_items[0].author)
        self.assertEqual(None, news_items[0].content)

        # Test last news item
        self.assertEqual("Fines for Vic leaders in nation’s protests",
                         news_items[-1].title)
        self.assertEqual("https://www.theaustralian.com.au/nation/coronavirus-australia-live-news-surprise-good-news-in-house-price-forecasts/news-story/e6f968a7397e7bee641c7ec37aff90e7",
                         news_items[-1].url)
        self.assertEqual("LIVE: CORONAVIRUS CRISIS", news_items[-1].topic)
        self.assertEqual("Angelica Snowden, Kieran Gair, Tessa Akerman", news_items[-1].author)
        self.assertEqual("Police praise peaceful marches by tens of thousands, but some Black Lives Matter protesters are pepper-sprayed and Victoria Police fine organisers.",
                         news_items[-1].content)


if __name__ == '__main__':
    unittest.main()
