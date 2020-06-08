from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.db_base import Base
from models.news_website import NewsWebsite


class NewsItem(Base):

    __tablename__ = "news_items"
    id = Column(Integer, primary_key=True)
    # The URL of a news item must be unique as it's the base of determining if a news item is updated/changed
    url = Column(String, unique=True, nullable=False)
    title = Column(String)
    content = Column(Text)
    author = Column(String)
    topic = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    news_website_id = Column(Integer, ForeignKey("news_websites.id"))
    news_website = relationship("NewsWebsite", back_populates="news_items")

    def __init__(self, url: str, title: str, content: str = None, author: str = None, topic: str = None,
                 news_website: NewsWebsite = None):
        """Representation of a news item

        :param url: URL to access the news item
        :param title: headline/title of the news item
        :param content: summary/content of the news item, None if unknown
        :param author: name of the author of the news item, None if unknown
        :param topic: topic of the news item, None if unknown
        :param news_website: NewsWebsite that this news item is associated with
        """
        self.url = url
        self.title = title
        self.content = content
        self.author = author
        self.topic = topic
        self.news_website = news_website
        time = datetime.now()
        self.created_at = time
        self.updated_at = time
