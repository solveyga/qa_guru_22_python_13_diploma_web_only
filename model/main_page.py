from selene import have
from selene.support.shared import browser
#from data.users import User, Gender, Hobby
import os
import allure
from selene.support.conditions import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from model.base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        self.slogan = s('//h1[contains(., "MyBook") and contains(., "слушайте")]')
        self.trial_button = s('button[type="button"].ant-btn.ant-btn-trial')
        self.search_input = s('.ant-input')

    def should_have_slogan(self, expected_slogan: str):
        self.slogan.should(have.exact_text(expected_slogan))

    def should_have_trial_button(self, expected_button_text: str):
        self.trial_button.should(have.exact_text(expected_button_text))

    def click_trial_button(self):
        self.trial_button.click()

    def search_book(self, query_string: str):
        self.search_input.type(query_string).press_enter()
