from bs4.element import ResultSet
from parsers.news_item_parser import NewsItemParser
from models.news_item import NewsItem


class AbcNewsItemParser(NewsItemParser):
    def __init__(self):
        """ Parses news items matching ABC News HTML structure
        """
        super().__init__()

    @staticmethod
    def __get_headline_elem(article: ResultSet):
        headline_elem = article.find('h3')
        return headline_elem

    @staticmethod
    def __get_headline_text(article: ResultSet):
        headline_elem = AbcNewsItemParser.__get_headline_elem(article)
        # Not all articles use a common headline element, if not found get the link text
        if headline_elem is None:
            headline_elem = article.find('a')
        return headline_elem.getText().strip()

    @staticmethod
    def __get_item_url(article: ResultSet):
        headline_elem = AbcNewsItemParser.__get_headline_elem(article)
        # Not all articles use a common headline element, so get first link if no dedicated headline encountered
        if headline_elem is None:
            return article.find('a')['href']
        else:
            return headline_elem.find('a')['href']

    @staticmethod
    def __get_item_author(article: ResultSet):
        byline = article.find(class_='byline')
        if byline is not None:
            return byline.find('a').getText().strip()
        else:
            return None

    def __get_page_articles(self, html):
        soup = super()._get_page_soup(html)
        # ToDo: also find separate video articles that have class 'doctype-video'
        return soup.find_all(class_='doctype-article')

    def get_news_items(self, html) -> [NewsItem]:
        news_items = []
        for article in self.__get_page_articles(html):
            news_items.append(
                NewsItem(
                    url=AbcNewsItemParser.__get_item_url(article),
                    title=AbcNewsItemParser.__get_headline_text(article),
                    author=AbcNewsItemParser.__get_item_author(article)
                )
            )
        return news_items
