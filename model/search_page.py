from selene import have
from selene.support.shared import browser
#from data.users import User, Gender, Hobby
import os
import allure
from selene.support.conditions import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from model.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self):
        self.title_elements = ss('.lnjchu-1.hhskLb')
        self.author_elements = ss('.dey4wx-1.jVKkXg')

    def should_have_first_title(self, expected_title: str):
        self.title_elements.first.should(have.exact_text(expected_title))

    def should_have_first_author(self, expected_author: str):
        self.author_elements.first.should(have.exact_text(expected_author))
