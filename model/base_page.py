from utils.accept_cookies import accept_cookies_if_present
from selene.support.shared import browser
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s

class BasePage:
    uri = "/"

    def open(self, uri = None):
        url = uri if uri is not None else self.uri
        browser.open(url)
        accept_cookies_if_present()

    def should_have_url_containing(self, expected_url: str):
        browser.should(have.url_containing(expected_url))

    def wait_for_loaded(self, expected_url = None):
        url = expected_url if expected_url else self.uri
        browser.should(have.url_containing(url))
        s('.sc-8xsh67-0.jeOLNX').should(be.visible)
