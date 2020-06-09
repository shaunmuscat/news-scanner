import unittest
from tests.helpers import get_test_data_file_contents
from parsers.abc_news_item_parser import AbcNewsItemParser


class TestAbcNewsItemParser(unittest.TestCase):
    def test_get_news_items(self):
        parser = AbcNewsItemParser()
        news_items = parser.get_news_items(get_test_data_file_contents("abc_news.html"))

        # Test first news item
        self.assertEqual("/news/2020-06-07/cormann-dubs-black-lives-matter-protesters-selfish-coronavirus/12330196",
                         news_items[0].url)
        self.assertEqual("Senior Government Minister slams 'selfish' Black Lives Matter protesters", news_items[0].title)
        self.assertEqual(None, news_items[0].author)
        self.assertEqual('Senior Federal Government Minister Mathias Cormann takes aim at Australian Black Lives Matter protesters, dubbing their actions "selfish", "self-indulgent" and "reckless" amid the deadly coronavirus pandemic.',
                         news_items[0].content)
        self.assertEqual(None, news_items[0].topic)

        # Test last news item
        self.assertEqual("Your best photos from the past week",
                         news_items[-1].title)
        self.assertEqual('/news/abcmyphoto/2020-06-05/your-best-photos-for-the-week-ending-june-5-2020/12322252',
                         news_items[-1].url)
        self.assertEqual(None, news_items[-1].author)
        self.assertEqual(None, news_items[-1].content)
        self.assertEqual(None, news_items[-1].topic)

        # Test item with author, iterate through news items until known news item with author is found
        expected_url = "/news/2020-06-07/wa-liberals-under-liza-harvey-losing-hope-of-winning-election/12299608"
        expected_title = "WA Liberals fear election loss"
        item = next((x for x in news_items if x.url == expected_url and x.title == expected_title), None)
        self.assertEqual(expected_title, item.title)
        self.assertEqual(expected_url, item.url)
        self.assertEqual("Jacob Kagi", item.author)
        self.assertEqual("The WA Liberals are rapidly losing hope of achieving an unlikely victory in the March election, writes Jacob Kagi.",
                         item.content)
        self.assertEqual(None, item.topic)


if __name__ == '__main__':
    unittest.main()
