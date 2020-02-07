import requests
import json

import logging
import sys
sys.path.append('..')

from .Controller import Controller
class MenuBarController:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.currencySelector = CurrencySelector.CurrencySelector(self)

    def configure_currency_list(self):
        pass
