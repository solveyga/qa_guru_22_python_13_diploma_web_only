import pytest
import allure
from model.search_page import SearchPage


@allure.story('Проверка поиска с главной страницы')
def test_search_prom_main_page(open_main_page):

    search_page = SearchPage()
    query_string = 'пикник на обочине'
    loaded_uri = '/search'
    expected_author = 'Аркадий и Борис Стругацкие'

    search_book(open_main_page, query_string, loaded_uri)
    check_search_results(search_page, query_string.capitalize(), expected_author)


@allure.step('Ввод строки в поиск')
def search_book(main_page, query_string, loaded_uri):
    main_page.search_book(query_string)
    main_page.wait_for_loaded(loaded_uri)

@allure.step('Проверить название и автора')
def check_search_results(search_page, expected_title, expected_author):
    search_page.should_have_first_title(expected_title)
    search_page.should_have_first_author(expected_author)
