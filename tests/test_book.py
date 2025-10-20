import pytest
import allure
from model.book_page import BookPage

@allure.story('Проверка обязательной регистрации для чтения бесплатной книги')
def test_free_book_page():
    book_page = BookPage()
    free_book_uri = '/author/ivan-sergeevich-turgenev/otcy-i-deti-1/'

    open_page(book_page, free_book_uri)


@allure.story('Проверка обязательной регистрации для чтения бесплатной книги')
def test_standard_book_page():
    book_page = BookPage()
    standard_book_uri = '/author/dzhordzh-oruell/1984/'

    open_page(book_page, standard_book_uri)


@allure.story('Проверка обязательной регистрации для чтения бесплатной книги')
def test_premium_book_page():
    book_page = BookPage()
    premium_book_uri = '/author/oskar-uajld/portret-doriana-greya-1/'

    open_page(book_page, premium_book_uri)


@allure.step('Открыть страницу книги')
def open_page(search_page, book_uri):
    search_page.open(book_uri)
    search_page.wait_for_loaded(book_uri)