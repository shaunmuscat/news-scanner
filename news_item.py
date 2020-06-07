from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

from db_base import Base


class NewsItem(Base):
    __tablename__ = 'news_items'

    id = Column(Integer, primary_key=True)
    website_name = Column(String)
    url = Column(String, unique=True)
    title = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, website_name, url, title):
        self.website_name = website_name
        self.url = url
        self.title = title
        time = datetime.now()
        self.created_at = time
        self.updated_at = time
