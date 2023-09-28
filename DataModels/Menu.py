from typing import List
from DataModels.MenuItem import MenuItem
class Menu:
    def __init__(self, name: str = "", dishes: List[MenuItem] = None):
        self.name = name
        if dishes is None:
            dishes = []
        self.dishes = dishes

    def addMenuItem(self, menu_item_name: str , menu_item_price: float):
        item = MenuItem(menu_item_name, menu_item_price)
        self.dishes.append(item)