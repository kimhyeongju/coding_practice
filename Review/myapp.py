import sys

class MenuItem:
    def __init__(self, title, action=None):
        self.title = title
        self.action = action

    def __str__(self):
        return "<MenuItem {self.title}>"

    def __repr__(self):
        return "<MenuItem {self.title}>"

    def run(self):
        self.action()

class Menu:
    def __init__(self):
        self.menus = []

    def add(self, menu_item):
        self.menus.append(menu_item)

    def print(self):
        print("[메뉴]", end="")
        for i, menu in enumerate(self.menus):
            print(f"{i}:{menu.title} ", end="")
        print()

    def run(self, select):
        if select >= len(self.menus):
            print("잘못된 메뉴 선택입니다.")
            return
        menu_item = self.menus[select]
        menu_item.run()

class Application:
    def __init__(self):
        self.menu = Menu()
        self.create_menu(self.menu)

    def create_menu(self, menu):
        pass

    def run(self):
        while True:
            self.menu.print()
            sel = int(input("선택] "))
            self.menu.run(sel)

if __name__ == "__main__":
    pass