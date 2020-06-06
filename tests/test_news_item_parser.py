import unittest
from pathlib import Path
from news_item_parser import NewsItemParser


class TestNewsItemParsing(unittest.TestCase):
    @staticmethod
    def get_news_items_from_file(file_name, item_elem, item_class, title_elem, title_class, url_elem, url_class):
        parser = NewsItemParser(item_elem, item_class, title_elem, title_class, url_elem, url_class)
        html_file = Path(__file__).parent / 'sample_news_pages' / file_name
        with open(html_file) as reader:
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


if __name__ == '__main__':
    unittest.main()
