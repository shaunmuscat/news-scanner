import schedule
import time
from datetime import datetime
from models.db_base import Session, engine, Base
from models.news_item import NewsItem
from models.news_website import NewsWebsite
from loggers.console_news_logger import ConsoleNewsLogger
from parsers import sbs_news_item_parser, abc_news_item_parser, nine_news_item_parser, the_australian_news_item_parser
from news_scanner import NewsScanner


def get_first_or_create_news_website(name: str, base_url: str, front_page_url: str) -> NewsWebsite:
    """Gets the first matching instance of a NewsWebsite from the db or creates one if none exist

    :param name: new website name
    :param base_url: base URL of new website
    :param front_page_url: URL of news website front page
    :return:
    """
    session = Session(expire_on_commit=False)
    website = session.query(NewsWebsite).filter_by(name=name, base_url=base_url, front_page_url=front_page_url).first()
    if website is None:
        website = NewsWebsite(name, base_url, front_page_url)
        session.add(website)
        session.commit()
    session.close()
    return website


def news_scan_job():
    """Scans each of the configured websites for news items, logs added or updated items and persists them to the db

    :return:
    """
    sbs_web = get_first_or_create_news_website("SBS News", "https://www.sbs.com.au", "https://www.sbs.com.au/news/")
    abc_web = get_first_or_create_news_website("ABC News", "https://www.abc.net.au", "https://www.abc.net.au/news/")
    nine_web = get_first_or_create_news_website("Nine News", "https://www.9news.com.au/", "https://www.9news.com.au/")
    aus_web = get_first_or_create_news_website("The Australian", "https://www.theaustralian.com.au/", "https://www.theaustralian.com.au/")

    news_scanners = [
        NewsScanner(sbs_web, sbs_news_item_parser.SbsNewsItemParser()),
        NewsScanner(abc_web, abc_news_item_parser.AbcNewsItemParser()),
        NewsScanner(nine_web, nine_news_item_parser.NineNewsItemParser()),
        NewsScanner(aus_web, the_australian_news_item_parser.TheAustralianNewsItemParser())
    ]

    session = Session()
    logger = ConsoleNewsLogger()
    logger.log_news_scan_starting(datetime.now())

    for scanner in news_scanners:
        for scanned_news_item in scanner.get_news_items():
            existing_item = session.query(NewsItem).filter(NewsItem.url == scanned_news_item.url,
                                                           NewsItem.news_website == scanner.news_website).first()

            if existing_item is None:
                scanned_news_item.news_website = scanner.news_website
                logger.log_news_item_added(scanned_news_item)
                session.add(scanned_news_item)
                session.commit()
            else:
                item_changed = False
                original_properties = {}
                if existing_item.title != scanned_news_item.title and scanned_news_item.title is not None:
                    item_changed = True
                    original_properties['title'] = existing_item.title
                    existing_item.title = scanned_news_item.title

                if existing_item.content != scanned_news_item.content and scanned_news_item.content is not None:
                    item_changed = True
                    original_properties['content'] = existing_item.content
                    existing_item.content = scanned_news_item.content

                if existing_item.author != scanned_news_item.author and scanned_news_item.author is not None:
                    item_changed = True
                    original_properties['author'] = existing_item.author
                    existing_item.author = scanned_news_item.author

                if existing_item.topic != scanned_news_item.topic and scanned_news_item.topic is not None:
                    item_changed = True
                    original_properties['topic'] = existing_item.topic
                    existing_item.topic = scanned_news_item.topic

                if item_changed:
                    existing_item.updated_at = datetime.now()
                    session.add(existing_item)
                    session.commit()
                    logger.log_news_item_updated(existing_item, original_properties)

    session.close()
    logger.log_news_scan_ending(datetime.now())


if __name__ == "__main__":
    # Generate db schema
    Base.metadata.create_all(engine)

    # Run initial news scan and then schedule the news scan to run at a regular basis thereafter
    news_scan_job()
    schedule.every(5).minutes.do(news_scan_job)

    while True:
        schedule.run_pending()
        time.sleep(1)
