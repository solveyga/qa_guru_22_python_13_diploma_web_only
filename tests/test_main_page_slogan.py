import allure
from selene.support.conditions import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.story('Проверка слогана на главной странице')
def test_github():
    browser.open("/")

    s('//h1[contains(., "MyBook") and contains(., "слушайте")]').should(have.exact_text('MyBook — читайте и слушайте по одной подписке'))
    # s('button[type="button"].ant-btn.ant-btn-trial').should(be.visible)
    s('button[type="button"].ant-btn.ant-btn-trial').should(have.exact_text('14 дней бесплатно'))
    s('button[type="button"].ant-btn.ant-btn-trial').click()
    browser.should(have.url_containing('/trial'))
