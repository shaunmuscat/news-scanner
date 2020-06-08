import unittest
from pathlib import Path


class TestNewsItemParser(unittest.TestCase):
    @staticmethod
    def get_page_html(filename):
        html_file = Path(__file__).parent / 'test_data' / filename
        with open(html_file, encoding='UTF-8') as reader:
            html = reader.read()
        return html
