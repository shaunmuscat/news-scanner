import unittest
from models.news_item import NewsItem


class TestNewsItem(unittest.TestCase):
    def test_attributes(self):
        self.assertEqual("news_items", NewsItem.__tablename__)
        assert hasattr(NewsItem, 'id')
        assert hasattr(NewsItem, 'url')
        assert hasattr(NewsItem, 'title')
        assert hasattr(NewsItem, 'content')
        assert hasattr(NewsItem, 'author')
        assert hasattr(NewsItem, 'topic')
        assert hasattr(NewsItem, 'created_at')
        assert hasattr(NewsItem, 'updated_at')
        assert hasattr(NewsItem, 'news_website_id')
        assert hasattr(NewsItem, 'news_website')


if __name__ == '__main__':
    unittest.main()
