import requests
from .models import Askstories, Showstories, Jobstories, Newstories

MODEL_LIST: list = [Askstories, Showstories, Newstories, Jobstories]


class HackerNews(object):
    default_cat = ["askstories", "showstories", "newstories", "jobstories"]

    def get_news(self, arg="", item_id=None):
        url = f'https://hacker-news.firebaseio.com/v0/{arg}.json'
        rec = requests.get(url=url)
        list_id_str = rec.text[1:-2].split(",")
        list_id_int = [int(i) for i in list_id_str]
        print(len(list_id_int))
        list_json = []
        for i in list_id_int:
            if i not in item_id:
                url = f'https://hacker-news.firebaseio.com/v0/item/{i}.json'
                rec = requests.get(url=url)
                list_json.append(rec.json())
                print(rec.json())
        return list_json


class DatabaseObjects(object):
    table_model = None

    def __value_checker(self, item, item_str: str):
        tmp_value = None

        if item_str in item.keys():
            tmp_value = item[item_str]

        return tmp_value

    def object_set_model(self, model):
        self.table_model = model

    def object_create(self, row):
        self.table_model.objects.get_or_create(by=self.__value_checker(row, 'by'),
                                               id_news=self.__value_checker(row, 'id'),
                                               time=self.__value_checker(row, 'time'),
                                               title=self.__value_checker(row, 'title'),
                                               text=self.__value_checker(row, 'text'),
                                               type=self.__value_checker(row, 'type'),
                                               url=self.__value_checker(row, 'url'))
