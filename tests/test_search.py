from time import sleep

import allure
from selene.support.conditions import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from model.main_page import MainPage


@allure.story('Проверка поиска с главной страницы')
def test_search_prom_main_page(open_main_page):

    main_page = MainPage()
    query_string = 'Пикник на обочине'

    search_book(open_main_page, query_string)
    # check_search_results(query_string)

    sleep(3)


@allure.step('Ввод строки в поиск')
def search_book(main_page, query_string):
    main_page.search_book(query_string)