import allure
from model.book_page import BookPage


@allure.story(
    "Проверка обязательной регистрации для чтения бесплатной книги неавторизованным пользователем"
)
def test_free_book_page(setup_browser):
    browser = setup_browser
    book_page = BookPage()
    free_book_uri = "/author/ivan-sergeevich-turgenev/otcy-i-deti-1/"
    title = "Отцы и дети"
    author = "Иван Тургенев"

    open_page(book_page, free_book_uri)
    check_title_and_author(book_page, title, author)
    check_email_is_requested(book_page)


@allure.story(
    "Проверка чтения фрагмента для книги из стандартной подписки неавторизованным пользователем"
)
def test_standard_book_page(setup_browser):
    browser = setup_browser
    book_page = BookPage()
    standard_book_uri = "/author/dzhordzh-oruell/1984/"
    title = "1984"
    author = "Джордж Оруэлл"

    open_page(book_page, standard_book_uri)
    check_title_and_author(book_page, title, author)
    check_read_and_subscription_buttons(book_page)
    check_reading(book_page, standard_book_uri)


@allure.story(
    "Проверка чтения фрагмента для книги из премиум подписки неавторизованным пользователем"
)
def test_premium_book_page(setup_browser):
    browser = setup_browser
    book_page = BookPage()
    premium_book_uri = "/author/oskar-uajld/portret-doriana-greya-1/"
    title = "Портрет Дориана Грея"
    author = "Оскар Уайльд"

    open_page(book_page, premium_book_uri)
    check_title_and_author(book_page, title, author)
    check_read_and_subscription_buttons(book_page)
    check_reading(book_page, premium_book_uri)


@allure.step("Открыть страницу книги")
def open_page(search_page, book_uri):
    search_page.open(book_uri)
    search_page.wait_for_loaded(book_uri)


@allure.step("Проверить название и автора")
def check_title_and_author(book_page, title, author):
    book_page.should_have_expected_title(title)
    book_page.should_have_expected_author(author)


@allure.step("Проверить запрос email для чтения")
def check_email_is_requested(book_page):
    book_page.should_be_email_requested()
    book_page.should_be_read_online_button()
    book_page.click_read_online_button()
    book_page.should_be_email_explain()


@allure.step("Проверить кнопки оформления подписки и чтения ознакомительного фрагмента")
def check_read_and_subscription_buttons(book_page):
    book_page.should_be_read_fragment_button()
    book_page.should_be_subscription_button()


@allure.step(
    "Проверить чтение ознакомительного фрагмента неавторизованным пользователем"
)
def check_reading(book_page, book_uri):
    book_page.click_read_fragment_button()
    book_page.wait_for_loaded(book_uri + "read")
