from bs4.element import ResultSet
from parsers.news_item_parser import NewsItemParser
from models.news_item import NewsItem


class SbsNewsItemParser(NewsItemParser):
    def __init__(self):
        """ Parses news items matching SBS News HTML structure
        """
        super().__init__()

    @staticmethod
    def __get_headline_elem(article: ResultSet):
        headline_elem = article.find(class_='headline', recursive=True)
        return headline_elem

    @staticmethod
    def __get_headline_text(article: ResultSet):
        return SbsNewsItemParser.__get_headline_elem(article).getText().strip()

    @staticmethod
    def __get_item_url(article: ResultSet):
        return SbsNewsItemParser.__get_headline_elem(article).find('a')['href']

    def __get_page_articles(self, html):
        soup = super()._get_page_soup(html)
        return soup.find_all('div', class_='preview')

    def get_news_items(self, html) -> [NewsItem]:
        news_items = []
        for article in self.__get_page_articles(html):
            news_items.append(
                NewsItem(
                    url=SbsNewsItemParser.__get_item_url(article),
                    title=SbsNewsItemParser.__get_headline_text(article)
                )
            )
        return news_items
