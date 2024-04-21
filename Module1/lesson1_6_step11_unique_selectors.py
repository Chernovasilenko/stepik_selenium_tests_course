import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

try:
    # ссылка для проверки первой версии формы
    link_v1 = 'http://suninjuly.github.io/registration1.html'
    # ссылка для проверки второй версии формы
    link_v2 = 'http://suninjuly.github.io/registration2.html'

    browser = webdriver.Chrome()
    browser.get(link_v2)

    first_name = browser.find_element(
        By.CSS_SELECTOR, '.first_block .first_class input'
    )
    first_name.send_keys('Ivan')
    last_name = browser.find_element(
        By.CSS_SELECTOR, '.first_block .second_class input'
    )
    last_name.send_keys('Ivanov')
    email = browser.find_element(
        By.CSS_SELECTOR, '.first_block .third_class input'
    )
    email.send_keys('Ivan@stepik.org')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
    assert 'Congratulations! You have successfully registered!' == welcome_text

# обработка исключения, когда элемент на странице не был найден
except NoSuchElementException as error:
    print(
        f'Возникла ошибка:\n{error}\n'
        'Элемент по селектору не был найден на странице.'
    )

# обработка исключения, когда текст после успешного заполнения формы
# не соотвествует ожидаемому
except AssertionError as error:
    print(
        f'Возникла ошибка:\n{error}\n'
        'Текст после заполнения формы не соответствует ожидаемому.'
    )

finally:
    time.sleep(10)
    browser.quit()
