import allure
from selene.support.conditions import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from model.main_page import MainPage


@allure.story('Проверка слогана на главной странице')
def test_main_page_slogan():
    main_page = MainPage()

    expected_slogan = 'MyBook — читайте и слушайте по одной подписке'
    expected_button_text = '14 дней бесплатно'
    expected_url = '/trial'

    open_page(main_page)
    check_slogan(main_page, expected_slogan)
    check_trial_button(main_page, expected_button_text)
    check_trial_url(main_page, expected_url)


@allure.step('Открыть страницу')
def open_page(main_page):
    main_page.open()

@allure.step('Проверить слоган')
def check_slogan(main_page, expected_slogan):
    main_page.should_have_slogan(expected_slogan)

@allure.step('Проверить текст на кнопке триала')
def check_trial_button(main_page, expected_button_text):
    main_page.should_have_trial_button(expected_button_text)

@allure.step('Проверить страницу, на которую ведет кнопка триала')
def check_trial_url(main_page, expected_url):
    main_page.click_trial_button()
    main_page.should_have_url_containing(expected_url)
