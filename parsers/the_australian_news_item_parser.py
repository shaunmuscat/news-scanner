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

    @staticmethod
    def __get_topic_text(article: ResultSet):
        topic = article.find(class_="story-block__kicker")
        if topic is not None:
            return topic.getText().strip()
        else:
            return None

    @staticmethod
    def __get_item_author(article: ResultSet):
        author = article.find(class_="author-block__info", recursive=True)
        if author is None:
            author = article.find(class_="story-block__byline", recursive=True)
        if author is not None:
            return author.getText().strip()
        else:
            return None

    @staticmethod
    def __get_item_content(article: ResultSet):
        content = article.find('p', class_="story-block__standfirst", recursive=True)
        if content is None:
            content = article.find('p', class_="standfirst-content", recursive=True)
        if content is None:
            content = article.find('p', class_=None)
        if content is not None:
            return content.getText().strip()
        else:
            return None

    def __get_page_articles(self, html):
        soup = super()._get_page_soup(html)
        return soup.find_all(class_="story-block")

    def get_news_items(self, html) -> [NewsItem]:
        news_items = []
        for article in self.__get_page_articles(html):
            news_items.append(
                NewsItem(
                    url=TheAustralianNewsItemParser.__get_item_url(article),
                    title=TheAustralianNewsItemParser.__get_headline_text(article),
                    content=TheAustralianNewsItemParser.__get_item_content(article),
                    author=TheAustralianNewsItemParser.__get_item_author(article),
                    topic=TheAustralianNewsItemParser.__get_topic_text(article)
                )
            )
        return news_items
