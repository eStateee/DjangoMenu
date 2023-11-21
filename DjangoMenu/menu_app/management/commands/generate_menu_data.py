import random
from string import ascii_letters, digits

from menu_app.models import Menu, MenuItem
from django.core.management.base import BaseCommand
from django.db import IntegrityError


ALPHABET = ascii_letters + digits


class Command(BaseCommand):
    _class = Menu
    name = 'MENU'
    menu_size: int = 3
    menu_depth: int = 3

    def create_menu_items(
        self,
        level_name: str,
        menu: Menu,
        parent: MenuItem = None,
        depth: int = 0,
    ) -> None:
        if depth >= self.menu_depth:
            try:
                menu_item = MenuItem.objects.create(
                    name='External link',
                    menu=menu,
                    parent=parent,
                )
                MenuItem.objects.create(
                    name='UpTrader',
                    menu=menu,
                    parent=menu_item,
                    url='https://uptrader.io/en/',
                )
            except IntegrityError:
                pass
            return
        for i in range(self.menu_size):
            unique_id = ''.join(random.choice(ALPHABET) for i in range(3))
            menu_item_name = (
                f'{level_name}: nested-{depth+1}_item-{i+1} {unique_id}')
            menu_item = MenuItem.objects.create(
                name=menu_item_name,
                menu=menu,
                parent=parent,
            )
            self.create_menu_items(level_name, menu, menu_item, depth + 1)

    def create_menu(self, menu_name: str) -> None:
        menu = Menu.objects.create(name=menu_name)
        self.create_menu_items(level_name=menu.name, menu=menu)


    def handle(self, *args, **kwargs):
        for menu_name in (
            'main_menu',
            'second_menu',
            'third_menu',
        ):
            self.create_menu(menu_name)
