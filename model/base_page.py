from utils.accept_cookies import accept_cookies_if_present
from selene.support.shared import browser

class BasePage:
    uri = "/"

    def open(self, uri=None):
        url = uri if uri is not None else self.uri
        browser.open(url)
        accept_cookies_if_present()

