from bs4.element import ResultSet
from parsers.news_item_parser import NewsItemParser
from models.news_item import NewsItem


class NineNewsItemParser(NewsItemParser):
    def __init__(self):
        """ Parses news items matching Nine News HTML structure
        """
        super().__init__()

    @staticmethod
    def __get_headline_text(article: ResultSet):
        return article.find(class_="story__headline__text").getText().strip()

    @staticmethod
    def __get_item_url(article: ResultSet):
        return article.find('a', class_="story__link")['href']

    def __get_page_articles(self, html):
        soup = super()._get_page_soup(html)
        return soup.find_all('article', class_="story-block")

    def get_news_items(self, html) -> [NewsItem]:
        news_items = []
        for article in self.__get_page_articles(html):
            news_items.append(
                NewsItem(
                    url=NineNewsItemParser.__get_item_url(article),
                    title=NineNewsItemParser.__get_headline_text(article)
                )
            )
        return news_items
