import json
import logging
import sys
from os import path

sys.path.append('..')

from views import Application
from views import About

from .Controller import Controller
from models import Item
from services import ItemsService
from models import categorie


def is_currency_saved():
    return path.exists("currency.json")


class MainController(Controller):
    logger = logging.getLogger(__name__)
    application: Application
    items : [Item]
    categoeries: []

    def __init__(self):
        super().__init__()
        self.items = []
        items = None
        self.categories = categorie.CATEGORIES

        if not is_currency_saved():
            self.logger.warning("Local currency data not found, load from POE api")
            self.load_from_api()
        else:
            self.logger.warning("Local currency found, load")
            if not self.load_currency_local():
                self.logger.warning("Local currency loading fail, load from POE api")
                self.load_from_api()

        if items or self.items:
            self.application = Application.Application(self)

            for item in self.items:
                self.application.add_items(item.name,item.type,item.id)
            self.application.start()
        else:
            self.logger.error("Connection error to poe API")

    def save_currency(self):
        try:
            f = open("currency.json", 'w')
            f.write("{\"items\" : [\n")
            for currency in self.items:
                f.write(json.dumps(currency.__dict__))
                if not currency is self.items[-1]:
                    f.write(",\n")
            f.write(']}')
            return True
        except Exception as error:
            return False

    def load_from_api(self):
        items = ItemsService.ItemsService.getCurrency()
        if items:
            self.items = [Item.Currency(item[0], item[1]) for item in items]
            self.save_currency()

    def load_currency_local(self):
        try:
            f = open("currencys.json", 'r')
            items = json.loads(f.read())
            for currency in items["items"]:
                self.items.append(Item.Currency(currency["name"],currency["id"]))
            return True
        except Exception as error:
            print(error)
            return False

    def quit(self):
        self.logger.info("Exit")
        sys.exit(1)

    def save(self):
        self.logger.info("Save action")

    def about(self):
        about = About.About(self)