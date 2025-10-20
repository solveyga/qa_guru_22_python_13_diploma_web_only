from selene import have
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss
from model.base_page import BasePage


class BookPage(BasePage):
    def __init__(self):
        self.title = s(".bzVsYa")
        self.author = s(".dey4wx-1.jVKkXg")
        self.email_required_field = s('input[type="email"]')
        self.read_online = s('button[type="button"].ant-btn-primary')
        self.read_fragment = s(".ant-btn-primary.ant-btn-lg.ant-btn-block")
        self.unauthorized_email_explain = s(".ant-form-item-explain")
        self.subscription_button = s(
            ".ant-btn.sc-1t4pdxh-0.kAlGSv.ant-btn-primary.ant-btn-lg"
        )

    def should_have_expected_title(self, expected_title: str):
        self.title.should(have.exact_text(expected_title))

    def should_have_expected_author(self, expected_author: str):
        self.author.should(have.exact_text(expected_author))

    def should_be_email_requested(self):
        self.email_required_field.should(be.visible)

    def should_be_read_online_button(self):
        self.read_online.should(be.visible)

    def click_read_online_button(self):
        self.read_online.click()

    def should_be_email_explain(self):
        self.unauthorized_email_explain.should(be.visible)

    def should_be_read_fragment_button(self):
        self.read_fragment.should(be.visible)

    def click_read_fragment_button(self):
        self.read_fragment.click()

    def should_be_subscription_button(self):
        self.subscription_button.should(be.visible)
