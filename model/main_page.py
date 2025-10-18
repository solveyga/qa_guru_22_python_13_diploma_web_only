from selene import have
from selene.support.shared import browser
#from data.users import User, Gender, Hobby
import os


class MainPage:
    def __init__(self):
        self.slogan = browser.element("#firstName")
        self.trial_button = browser.element("#firstName")

    def open(self):
        browser.open("/")