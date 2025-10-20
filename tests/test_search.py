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

@allure.story('Проверка элементов на странице поиска')
def test_search_page_elements():
    search_page = SearchPage()

    open_page(search_page)
    check_navigation_tabs(search_page)
    check_sections(search_page)


@allure.step('Ввести строку в поиск')
def search_book(main_page, query_string, loaded_uri):
    main_page.search_book(query_string)
    main_page.wait_for_loaded(loaded_uri)

@allure.step('Проверить название и автора')
def check_search_results(search_page, expected_title, expected_author):
    search_page.should_have_first_title(expected_title)
    search_page.should_have_first_author(expected_author)

@allure.step('Открыть страницу поиска')
def open_page(search_page):
    search_page.open()
    search_page.wait_for_loaded()

@allure.step('Проверить вкладку навигации')
def check_navigation_tabs(search_page):
    search_page.should_be_visible_navigation_tab()
    search_page.should_have_expected_tabs_count()
    search_page.tabs_should_have_expected_names()
    search_page.only_first_tab_should_be_disabled()

@allure.step('Проверить разделы: названия и наличие элементов')
def check_sections(search_page):
    search_page.should_be_all_sections()
