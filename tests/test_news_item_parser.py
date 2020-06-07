import unittest
from pathlib import Path
from news_item_parser import NewsItemParser


class TestNewsItemParsing(unittest.TestCase):
    @staticmethod
    def get_news_items_from_file(file_name, item_elem, item_class, title_elem, title_class, url_elem, url_class):
        parser = NewsItemParser(item_elem, item_class, title_elem, title_class, url_elem, url_class)
        html_file = Path(__file__).parent / 'sample_news_pages' / file_name
        with open(html_file, encoding='UTF-8') as reader:
            raw_html = reader.read()
            news_items = parser.find_news_items(raw_html)
        return parser, news_items

    @staticmethod
    def get_generic_news_items():
        return TestNewsItemParsing.get_news_items_from_file('generic.html', 'div', 'article', 'h3', 'headline', 'a', None)

    def test_news_items_found(self):
        parser, news_items = TestNewsItemParsing.get_generic_news_items()
        self.assertEqual(len(news_items), 4)

    def test_get_item_url(self):
        parser, news_items = TestNewsItemParsing.get_generic_news_items()
        self.assertEqual('/news/us-protests', parser.get_item_url(news_items[0]))
        self.assertEqual('/news/where-are-the-bees', parser.get_item_url(news_items[1]))
        self.assertEqual('/news/australia-attending-g7', parser.get_item_url(news_items[2]))
        self.assertEqual('/news/winter-comfort-food', parser.get_item_url(news_items[3]))

    def test_get_item_title(self):
        parser, news_items = TestNewsItemParsing.get_generic_news_items()
        self.assertEqual('Protests ongoing in the US!', parser.get_item_title(news_items[0]))
        self.assertEqual('Where have the bees gone?', parser.get_item_title(news_items[1]))
        self.assertEqual('Australia to attend the G7 summit...', parser.get_item_title(news_items[2]))
        self.assertEqual('Tasty comfort food for keeping warm', parser.get_item_title(news_items[3]))

    def test_parse_sbs_news(self):
        # Use None for title elem since new items can have title within <p> if article or <h3> if video
        parser, news_items = TestNewsItemParsing.get_news_items_from_file('sbs_news.html', 'div', 'preview__wrap', None,
                                                                          'headline', 'a', None)

        # Page contains 51 unique news items, 1 repeated video (active carousel), and 1 repeated (inactive) article
        self.assertEqual(len(news_items), 53)
        self.assertEqual('Two men charged after Sydney anti-racism protests', parser.get_item_title(news_items[0]))
        self.assertEqual('/news/two-men-charged-after-sydney-anti-racism-protests', parser.get_item_url(news_items[0]))
        self.assertEqual("There are fears coronavirus is stopping Australia's migrant women from accessing abortions",
                         parser.get_item_title(news_items[-1]))
        self.assertEqual('/news/there-are-fears-coronavirus-is-stopping-australia-s-migrant-women-from-accessing-abortions',
                         parser.get_item_url(news_items[-1]))

    def test_parse_abc_news(self):
        # Use None for item elem since items can be <li> or <div>
        parser, news_items = TestNewsItemParsing.get_news_items_from_file('abc_news.html', None, 'doctype-article',
                                                                          'h3', None, 'a', None)

        self.assertEqual("Senior Government Minister slams 'selfish' Black Lives Matter protesters",
                         parser.get_item_title(news_items[0]))
        self.assertEqual('/news/2020-06-07/cormann-dubs-black-lives-matter-protesters-selfish-coronavirus/12330196',
                         parser.get_item_url(news_items[0]))
        self.assertEqual("Your best photos from the past week", parser.get_item_title(news_items[-1]))
        self.assertEqual('/news/abcmyphoto/2020-06-05/your-best-photos-for-the-week-ending-june-5-2020/12322252',
                         parser.get_item_url(news_items[-1]))

    def test_parse_nine_news(self):
        parser, news_items = TestNewsItemParsing.get_news_items_from_file('nine_news.html', 'article', 'story-block',
                                                                          'h3', 'story__headline', 'a', 'story__link')

        self.assertEqual("Two missing after fire rips through home", parser.get_item_title(news_items[0]))
        self.assertEqual('https://www.9news.com.au/national/tyaak-house-fire-eleven-hospitalised-two-unaccounted-for/60155f9d-948f-4cc0-a361-14f01bdae415',
                         parser.get_item_url(news_items[0]))
        self.assertEqual("Thousands rally in US capital on 12th day of George Floyd protests",
                         parser.get_item_title(news_items[-1]))
        self.assertEqual('https://www.9news.com.au/world/george-floyd-protests-thousands-fill-washington-streets/598469e1-2a3e-4b74-8aec-d292c45e7e9c',
                         parser.get_item_url(news_items[-1]))

    def test_parse_the_australian(self):
        parser, news_items = TestNewsItemParsing.get_news_items_from_file('the_australian.html', 'div', 'story-block',
                                                                          'h3', 'story-block__heading', 'a', None)

        self.assertEqual("First new case in ACT in more than a month", parser.get_item_title(news_items[0]))
        self.assertEqual('https://www.theaustralian.com.au/nation/coronavirus-australia-live-news-health-officials-fear-second-covid19-spike-after-black-lives-matter-protests/news-story/6ee48b5a626d2391217e59c9ada2c632?keyevent=1.05pm',
                         parser.get_item_url(news_items[0]))
        self.assertEqual("Fines for Vic leaders in nation’s protests", parser.get_item_title(news_items[-1]))
        self.assertEqual('https://www.theaustralian.com.au/nation/coronavirus-australia-live-news-surprise-good-news-in-house-price-forecasts/news-story/e6f968a7397e7bee641c7ec37aff90e7',
                         parser.get_item_url(news_items[-1]))


if __name__ == '__main__':
    unittest.main()
