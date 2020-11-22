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