from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selene.support.shared import browser

def accept_cookies_if_present(timeout=1):
    try:
        WebDriverWait(browser.driver, timeout).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[./span[text()='Принять']]")
            )
        ).click()
    except Exception:
        pass
