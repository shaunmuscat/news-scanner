from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from models.db_base import Base


class NewsWebsite(Base):

    __tablename__ = "news_websites"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    base_url = Column(String)
    front_page_url = Column(String, unique=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    news_items = relationship("NewsItem", back_populates="news_website")

    def __init__(self, name: str, base_url: str, front_page_url: str):
        """Representation of a news website

        :param name: name of the news website
        :param base_url: base URL of the news website
        :param front_page_url: URL of the news website front page
        """
        self.name = name
        self.base_url = base_url
        self.front_page_url = front_page_url
        time = datetime.now()
        self.created_at = time
        self.updated_at = time
