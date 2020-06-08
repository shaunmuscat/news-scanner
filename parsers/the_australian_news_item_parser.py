from bs4.element import ResultSet
from parsers.news_item_parser import NewsItemParser
from models.news_item import NewsItem


class TheAustralianNewsItemParser(NewsItemParser):
    def __init__(self):
        """ Parses news items matching The Australian HTML structure
        """
        super().__init__()

    @staticmethod
    def __get_headline_elem(article: ResultSet):
        # Article can sometimes have no headline, e.g. in Daily Cartoon
        return article.find(class_="story-block__heading")

    @staticmethod
    def __get_headline_text(article: ResultSet):
        headline = TheAustralianNewsItemParser.__get_headline_elem(article)
        if headline is None:
            return None
        else:
            return headline.getText().strip()

    @staticmethod
    def __get_item_url(article: ResultSet):
        headline = TheAustralianNewsItemParser.__get_headline_elem(article)
        if headline is None:
            return article.find('a')['href']
        else:
            return headline.find('a')['href']

    def __get_page_articles(self, html):
        soup = super()._get_page_soup(html)
        return soup.find_all(class_="story-block")

    def get_news_items(self, html) -> [NewsItem]:
        news_items = []
        for article in self.__get_page_articles(html):
            news_items.append(
                NewsItem(
                    url=TheAustralianNewsItemParser.__get_item_url(article),
                    title=TheAustralianNewsItemParser.__get_headline_text(article)
                )
            )
        return news_items
