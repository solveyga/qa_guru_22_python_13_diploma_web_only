from selene import have
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss
from model.base_page import BasePage


class BookPage(BasePage):
    def __init__(self):
        self.title_elements = ss('.lnjchu-1.hhskLb')

