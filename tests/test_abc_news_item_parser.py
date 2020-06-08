import unittest
from tests.test_news_item_parser import TestNewsItemParser
from parsers.abc_news_item_parser import AbcNewsItemParser


class TestAbcNewsItemParser(TestNewsItemParser):
    def test_get_news_items(self):
        parser = AbcNewsItemParser()
        news_items = parser.get_news_items(self.get_page_html("abc_news.html"))

        # Test first news item
        self.assertEqual("/news/2020-06-07/cormann-dubs-black-lives-matter-protesters-selfish-coronavirus/12330196", news_items[0].url)
        self.assertEqual("Senior Government Minister slams 'selfish' Black Lives Matter protesters", news_items[0].title)

        # Test last news item
        self.assertEqual("Your best photos from the past week",
                         news_items[-1].title)
        self.assertEqual('/news/abcmyphoto/2020-06-05/your-best-photos-for-the-week-ending-june-5-2020/12322252',
                         news_items[-1].url)


if __name__ == '__main__':
    unittest.main()
