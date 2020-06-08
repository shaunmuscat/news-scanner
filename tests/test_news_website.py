import unittest
from models.news_website import NewsWebsite


class TestNewsWebsite(unittest.TestCase):
    def test_attributes(self):
        self.assertEqual("news_websites", NewsWebsite.__tablename__)
        assert hasattr(NewsWebsite, 'id')
        assert hasattr(NewsWebsite, 'name')
        assert hasattr(NewsWebsite, 'base_url')
        assert hasattr(NewsWebsite, 'front_page_url')
        assert hasattr(NewsWebsite, 'created_at')
        assert hasattr(NewsWebsite, 'updated_at')
        assert hasattr(NewsWebsite, 'news_items')


if __name__ == '__main__':
    unittest.main()
