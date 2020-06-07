import requests
import datetime
import schedule
import time

from news_item_parser import NewsItemParser
from db_base import Session, engine, Base
from news_item import NewsItem


class NewsScanner:
    def __init__(self, website_name: str, url: str, news_parser: NewsItemParser):
        self.website_name = website_name
        self.url = url
        self.news_item_parser = news_parser

    def get_web_page_content(self):
        r = requests.get(self.url, timeout=5)
        return r.content

    def get_news_items(self):
        items = self.news_item_parser.find_news_items(self.get_web_page_content())
        scanned_items = []
        for item in items:
            scanned_items.append({
                'time': datetime.datetime.now(),
                'website name': self.website_name,
                'url': self.news_item_parser.get_item_url(item),
                'title': self.news_item_parser.get_item_title(item)
            })
        return scanned_items


def news_scan_job():
    session = Session()

    news_scanners = {
        # ToDo: update as SBS doesn't always return right url, occasionally gets topic region url for multiple news items e.g. /news/topic/australia
        "sbs": NewsScanner("SBS News", "https://www.sbs.com.au/news/",
                           NewsItemParser('div', 'preview__wrap', None, 'headline', 'a', None)),
        # ToDo: update as ABC doesn't always return right title, occasionally gets correct title for url then in same page another item with title 'None' for same url
        # ToDo: update also as sometimes parser gets more than one article with same url, resulting in updated item within same scan
        "abc": NewsScanner("ABC News", "https://www.abc.net.au/news/",
                           NewsItemParser(None, 'doctype-article', 'h3', None, 'a', None)),
        # ToDo: update also as sometimes parser gets more than one article with same url, resulting in updated item within same scan
        "nine": NewsScanner("Nine News", "https://www.9news.com.au/",
                            NewsItemParser('article', 'story-block', 'h3', 'story__headline', 'a', 'story__link')),
        # ToDo: update also as sometimes parser gets more than one article with same url, resulting in updated item within same scan
        "australian": NewsScanner("The Australian", "https://www.theaustralian.com.au/",
                                  NewsItemParser('div', 'story-block', 'h3', 'story-block__heading', 'a', None))
    }

    print("<<<<<<<<<<>>>>>>>>>>")
    print("Starting news scan job at: {}".format(datetime.datetime.now()))

    for k, scanner in news_scanners.items():
        added = 0
        updated = 0

        print("================")
        print("Scanning: {}".format(scanner.website_name))
        print("================")

        for scanner_item in scanner.get_news_items():
            # ToDo: consider whether url is fully qualified
            existing_item = session.query(NewsItem).filter(NewsItem.url == scanner_item.get('url')).first()
            if existing_item is None:
                print("--------------")
                print("New item added")
                # ToDo: add check to add base to url if not fully qualified
                news_item = NewsItem(scanner_item.get('website name'), scanner_item.get('url'),
                                     scanner_item.get('title'))
                print("Time: {}".format(news_item.created_at))
                print("Website: {}".format(news_item.website_name))
                print("URL: {}".format(news_item.url))
                print("Content: {}".format(news_item.title))
                print("--------------")
                session.add(news_item)
                session.commit()
                added += 1
            else:
                if existing_item.title != scanner_item.get('title'):
                    print("--------------")
                    print('title changed from: "{}" to: "{}"'.format(existing_item.title, scanner_item.get('title')))
                    print("--------------")
                    print("Existing item updated")
                    existing_item.updated_at = datetime.datetime.now()
                    print("Time: {}".format(existing_item.updated_at))
                    print("Website: {}".format(existing_item.website_name))
                    print("URL: {}".format(existing_item.url))
                    existing_item.title = scanner_item.get('title')
                    print("Content: {}".format(existing_item.title))
                    print("--------------")
                    session.add(existing_item)
                    session.commit()
                    updated += 1

        print("================")
        print(scanner.website_name)
        print('New items added: {}'.format(added))
        print('Existing items updated: {}'.format(updated))
        print("================")

    session.close()

    print("Ending news scan job at: {}".format(datetime.datetime.now()))
    print("<<<<<<<<<<>>>>>>>>>>")


if __name__ == "__main__":
    # Generate db schema
    Base.metadata.create_all(engine)

    # Run initial news scan and then schedule the news scan to run at a regular basis thereafter
    news_scan_job()
    schedule.every(45).seconds.do(news_scan_job)

    while True:
        schedule.run_pending()
        time.sleep(1)
