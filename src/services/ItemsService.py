import requests
import json

class ItemsService:
    url_get_currency = "https://api.poe.watch/get?category=currency&league=Metamorph"
    url_get_item = "https://api.poe.watch/get?category=currency&league=Metamorph&id="

    @staticmethod
    def getCurrency():
        try:
            response = requests.get(ItemsService.url_get_currency)
            if response.status_code == 200:
                return [[currency["name"], currency["id"]] for currency in response.json()]
        except requests.exceptions.ConnectionError:
            return None
        return None

    @staticmethod
    def getItem(id):
        response = requests.get(ItemsService.url_get_item + str(id))
        if response.status_code == 200:
            return response.json()
        else:
            return None