import logging
import sys
sys.path.append('..')

from views import Application
from .Controller import Controller
from models import Item
from services import ItemsService

class MainController(Controller):
    logger = logging.getLogger(__name__)
    application: Application
    items : [Item]

    def __init__(self):
        super().__init__()

        items = ItemsService.ItemsService.getCurrency()
        self.items = [Item.Currency(item[0],item[1]) for item in items]
        self.application = Application.Application(self)

        for item in self.items:
            self.application.add_items(item.name,item.type,item.id)
        self.application.start()

    def quit(self):
        self.logger.info("Exit")
        sys.exit(1)

    def save(self):
        self.logger.info("Save action")
