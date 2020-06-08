import requests
import schedule
import time

from news_item_parser import NewsItemParser
from datetime import datetime
from models.db_base import Session, engine, Base
from models.news_item import NewsItem
from models.news_website import NewsWebsite
from loggers.console_news_logger import ConsoleNewsLogger


class NewsScanner:
    def __init__(self, news_website: NewsWebsite, news_parser: NewsItemParser):
        self.news_website = news_website
        self.news_item_parser = news_parser

    def get_web_page_content(self):
        r = requests.get(self.news_website.front_page_url, timeout=5)
        return r.content

    def get_news_items(self):
        items = self.news_item_parser.find_news_items(self.get_web_page_content())
        scanned_items = []
        for item in items:
            scanned_items.append({
                'time': datetime.now(),
                'website name': self.news_website.name,
                'url': self.news_item_parser.get_item_url(item),
                'title': self.news_item_parser.get_item_title(item)
            })
        return scanned_items


def get_first_or_create_news_website(name: str, base_url: str, front_page_url: str) -> NewsWebsite:
    session = Session(expire_on_commit=False)
    website = session.query(NewsWebsite).filter_by(name=name, base_url=base_url, front_page_url=front_page_url).first()
    if website is None:
        website = NewsWebsite(name, base_url, front_page_url)
        session.add(website)
        session.commit()
    session.close()
    return website


def news_scan_job():
    sbs_web = get_first_or_create_news_website("SBS News", "https://www.sbs.com.au", "https://www.sbs.com.au/news/")
    abc_web = get_first_or_create_news_website("ABC News", "https://www.abc.net.au", "https://www.abc.net.au/news/")
    nine_web = get_first_or_create_news_website("Nine News", "https://www.9news.com.au/", "https://www.9news.com.au/")
    aus_web = get_first_or_create_news_website("The Australian", "https://www.theaustralian.com.au/", "https://www.theaustralian.com.au/")

    news_scanners = {
        # ToDo: update as SBS doesn't always return right url, occasionally gets topic region url for multiple news items e.g. /news/topic/australia
        "sbs": NewsScanner(sbs_web, NewsItemParser('div', 'preview__wrap', None, 'headline', 'a', None)),
        # ToDo: update as ABC doesn't always return right title, occasionally gets correct title for url then in same page another item with title 'None' for same url
        # ToDo: update also as sometimes parser gets more than one article with same url, resulting in updated item within same scan
        "abc": NewsScanner(abc_web, NewsItemParser(None, 'doctype-article', 'h3', None, 'a', None)),
        # ToDo: update also as sometimes parser gets more than one article with same url, resulting in updated item within same scan
        "nine": NewsScanner(nine_web, NewsItemParser('article', 'story-block', 'h3', 'story__headline', 'a', 'story__link')),
        # ToDo: update also as sometimes parser gets more than one article with same url, resulting in updated item within same scan
        "australian": NewsScanner(aus_web, NewsItemParser('div', 'story-block', 'h3', 'story-block__heading', 'a', None))
    }

    session = Session()
    logger = ConsoleNewsLogger()
    logger.log_news_scan_starting(datetime.now())

    for k, scanner in news_scanners.items():
        for scanner_item in scanner.get_news_items():
            # ToDo: consider whether url is fully qualified
            existing_item = session.query(NewsItem).filter(NewsItem.url == scanner_item.get('url'),
                                                           NewsItem.news_website == scanner.news_website).first()
            if existing_item is None:
                # ToDo: add check to add base to url if not fully qualified
                news_item = NewsItem(scanner_item.get('url'), scanner_item.get('title'), None, None, None,
                                     scanner.news_website)
                logger.log_news_item_added(news_item)
                session.add(news_item)
                session.commit()
            else:
                if existing_item.title != scanner_item.get('title'):
                    existing_item.title = scanner_item.get('title')
                    existing_item.updated_at = datetime.now()
                    logger.log_news_item_updated(existing_item, {'title': scanner_item.get('title')})
                    session.add(existing_item)
                    session.commit()

    session.close()
    logger.log_news_scan_ending(datetime.now())


if __name__ == "__main__":
    # Generate db schema
    Base.metadata.create_all(engine)

    # Run initial news scan and then schedule the news scan to run at a regular basis thereafter
    news_scan_job()
    schedule.every(45).seconds.do(news_scan_job)

    while True:
        schedule.run_pending()
        time.sleep(1)
