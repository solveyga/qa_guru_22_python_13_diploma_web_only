import pytest
import allure
from model.main_page import MainPage


@allure.story('Проверка поиска с главной страницы')
def test_search_prom_main_page(open_main_page):

    main_page = MainPage()
    query_string = 'Пикник на обочине'
    loaded_uri = '/search'

    search_book(open_main_page, query_string, loaded_uri)
    # check_search_results(query_string)



@allure.step('Ввод строки в поиск')
def search_book(main_page, query_string, loaded_uri):
    main_page.search_book(query_string)
    main_page.wait_for_loaded(loaded_uri)