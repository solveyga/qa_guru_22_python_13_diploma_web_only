from selene import have
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss
from model.base_page import BasePage


class SearchPage(BasePage):

    uri = "/search"
    expected_tab_names = [
        "Все",
        "книги",
        "аудиокниги",
        "авторы",
        "серии",
        "жанры и темы",
    ]

    def __init__(self):
        self.title_elements = ss(".lnjchu-1.hhskLb")
        self.author_elements = ss(".dey4wx-1.jVKkXg")
        self.tabs = ss(".swiper-wrapper > .swiper-slide")
        self.sections = ss("div.sc-1bmhumr-2.eqAUoB")

    def should_have_first_title(self, expected_title: str):
        self.title_elements.first.should(have.exact_text(expected_title))

    def should_have_first_author(self, expected_author: str):
        self.author_elements.first.should(have.exact_text(expected_author))

    def should_be_visible_navigation_tab(self):
        for tab in self.tabs:
            tab.should(be.visible)

    def should_have_expected_tabs_count(self):
        self.tabs.should(have.size(len(self.expected_tab_names)))

    def tabs_should_have_expected_names(self):
        for i, name in enumerate(self.expected_tab_names):
            self.tabs[i].should(have.exact_text(name))

    def only_first_tab_should_be_disabled(self):
        first_tab_content = self.tabs[0].element("div.sc-11o5u18-1.ljhOrz")
        first_tab_content.should(have.attribute("disabled"))

    def should_be_all_sections(self):
        for i, name in enumerate(self.expected_tab_names[1:]):
            self.sections[i].should(have.text(name))
