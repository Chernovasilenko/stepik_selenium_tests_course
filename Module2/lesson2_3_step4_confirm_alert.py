import math
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = 'http://suninjuly.github.io/alert_accept.html'

    browser = webdriver.Chrome()
    browser.get(url)

    start_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    start_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value.nowrap')
    y = calc(x_element.text)

    answer = browser.find_element(By.CSS_SELECTOR, '.form-control')
    answer.send_keys(y)

    fin_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    fin_button.click()

except NoSuchElementException as error:
    print(
        f'Возникла ошибка:\n{error}\n'
        'Элемент по селектору не был найден на странице.'
    )

finally:
    time.sleep(10)
    browser.quit()
