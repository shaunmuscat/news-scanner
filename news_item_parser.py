from bs4 import BeautifulSoup


class NewsItemParser:
    def __init__(self, item_elem, item_class, title_elem, title_class, url_elem, url_class):
        self.item_elem = item_elem
        self.item_class = item_class
        self.title_elem = title_elem
        self.title_class = title_class
        self.url_elem = url_elem
        self.url_class = url_class

    def find_news_items(self, raw_html):
        html = BeautifulSoup(raw_html, 'html.parser')
        if self.item_class is None:
            return html.findAll(self.item_elem)
        else:
            return html.findAll(self.item_elem, class_=self.item_class)

    def get_item_url(self, news_item):
        if self.url_class is None:
            return news_item.find(self.url_elem)['href']
        else:
            return news_item.find(self.url_elem, class_=self.url_class)['href']

    def get_item_title(self, news_item):
        return self.get_component_text(news_item, self.title_elem, self.title_class)

    @staticmethod
    def get_component_text(news_item, component_elem, component_class):
        if component_class is None:
            component = news_item.find(component_elem)
        else:
            component = news_item.find(component_elem, class_=component_class)
        if component is not None:
            return component.getText().strip()
        else:
            return None
