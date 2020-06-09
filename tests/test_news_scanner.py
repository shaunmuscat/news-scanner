from unittest import TestCase
from unittest.mock import MagicMock
from news_scanner import NewsScanner
from models.news_website import NewsWebsite
from models.news_item import NewsItem
from parsers.abc_news_item_parser import AbcNewsItemParser
from parsers.sbs_news_item_parser import SbsNewsItemParser
from parsers.nine_news_item_parser import NineNewsItemParser
from parsers.the_australian_news_item_parser import TheAustralianNewsItemParser
from tests.helpers import get_test_data_file_contents


class TestNewsScanner(TestCase):
    def test_get_news_items(self):
        # Test NewsScanner on ABC News
        abc_news_scanner = NewsScanner(
            NewsWebsite("ABC News", "https://www.abc.net.au", "https://www.abc.net.au/news/"),
            AbcNewsItemParser())
        # Mock scanner object web scan to return HTML from test data file
        html = get_test_data_file_contents('abc_news_short.html')
        abc_news_scanner._get_web_page_content = MagicMock(return_value=html)
        expected_news_item = NewsItem(
            # expect NewsItem url to become absolute/fully-qualified
            url="https://www.abc.net.au"+"/news/2020-06-07/cormann-dubs-black-lives-matter-protesters-selfish-coronavirus/12330196",
            title="Senior Government Minister slams 'selfish' Black Lives Matter protesters",
            content='Senior Federal Government Minister Mathias Cormann takes aim at Australian Black Lives Matter protesters, dubbing their actions "selfish", "self-indulgent" and "reckless" amid the deadly coronavirus pandemic.',
            author=None,
            topic=None
        )
        actual_news_item = abc_news_scanner.get_news_items()[0]
        self.assertEqual(expected_news_item.url, actual_news_item.url)
        self.assertEqual(expected_news_item.title, actual_news_item.title)
        self.assertEqual(expected_news_item.content, actual_news_item.content)
        self.assertEqual(expected_news_item.author, actual_news_item.author)
        self.assertEqual(expected_news_item.topic, actual_news_item.topic)

        # Test NewsScanner on Nine News
        nine_news_scanner = NewsScanner(
            NewsWebsite("Nine News", "https://www.9news.com.au/", "https://www.9news.com.au/"),
            NineNewsItemParser()
        )
        html = get_test_data_file_contents('nine_news_short.html')
        nine_news_scanner._get_web_page_content = MagicMock(return_value=html)
        expected_news_item = NewsItem(
            # expect NewsItem url to remain unchanged as is already absolute/fully-qualified
            url="https://www.9news.com.au/national/sydney-protest-town-hall-station-closed-due-to-illegal-black-lives-matter-protest-in-the-cdb/75c4bf88-81d5-49cd-a59d-a30f942b73b7",
            title="Roads close and transport disrupted in cities as thousands protest",
            content=None,
            author=None,
            topic=None
        )
        actual_news_item = nine_news_scanner.get_news_items()[0]
        self.assertEqual(expected_news_item.url, actual_news_item.url)
        self.assertEqual(expected_news_item.title, actual_news_item.title)
        self.assertEqual(expected_news_item.content, actual_news_item.content)
        self.assertEqual(expected_news_item.author, actual_news_item.author)
        self.assertEqual(expected_news_item.topic, actual_news_item.topic)

        # Test NewsScanner on SBS News
        sbs_news_scanner = NewsScanner(
            NewsWebsite("SBS News", "https://www.sbs.com.au", "https://www.sbs.com.au/news/"),
            SbsNewsItemParser()
        )
        html = get_test_data_file_contents('sbs_news_short.html')
        sbs_news_scanner._get_web_page_content = MagicMock(return_value=html)
        expected_news_item = NewsItem(
            # expect NewsItem url to become absolute/fully-qualified
            url="https://www.sbs.com.au"+"/news/the-feed/most-african-americans-don-t-suffer-daily-shocking-racism-is-that-true",
            title="‘Most African Americans don’t suffer daily shocking racism.’ Is that true?",
            content=None,
            author=None,
            topic=None
        )
        actual_news_item = sbs_news_scanner.get_news_items()[0]
        self.assertEqual(expected_news_item.url, actual_news_item.url)
        self.assertEqual(expected_news_item.title, actual_news_item.title)
        self.assertEqual(expected_news_item.content, actual_news_item.content)
        self.assertEqual(expected_news_item.author, actual_news_item.author)
        self.assertEqual(expected_news_item.topic, actual_news_item.topic)

        # Test NewsScanner on The Australian
        the_australian_news_scanner = NewsScanner(
            NewsWebsite("The Australian", "https://www.theaustralian.com.au/", "https://www.theaustralian.com.au/"),
            TheAustralianNewsItemParser()
        )
        html = get_test_data_file_contents('the_australian_short.html')
        the_australian_news_scanner._get_web_page_content = MagicMock(return_value=html)
        expected_news_item = NewsItem(
            # expect NewsItem url to reamin unchanged as it is already absolute/fully-qualified
            url="https://www.theaustralian.com.au/weekend-australian-magazine/cool-in-a-crisis-jane-halton-leads-the-charge-for-coronavirus-vaccine/news-story/0c28ef3ba39fad19a2ecb0bd11f3e0fe",
            title="‘We dodged a bullet? Don’t kid yourself’",
            content="Spearheading the global race to find and distribute a COVID vaccine, Jane Halton has a warning that should make Australians listen.",
            author="By Megan Lehmann",
            topic="magazine"
        )
        actual_news_item = the_australian_news_scanner.get_news_items()[0]
        self.assertEqual(expected_news_item.url, actual_news_item.url)
        self.assertEqual(expected_news_item.title, actual_news_item.title)
        self.assertEqual(expected_news_item.content, actual_news_item.content)
        self.assertEqual(expected_news_item.author, actual_news_item.author)
        self.assertEqual(expected_news_item.topic, actual_news_item.topic)
