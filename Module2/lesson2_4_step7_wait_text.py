import math
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = 'http://suninjuly.github.io/explicit_wait2.html'

    browser = webdriver.Chrome()
    browser.get(url)

    # book_button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element(By.ID, 'book').click()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value.nowrap')
    y = calc(x_element.text)

    answer = browser.find_element(By.CSS_SELECTOR, '.form-control')
    answer.send_keys(y)

    submit_button = browser.find_element(By.ID, 'solve')
    browser.execute_script(
            'return arguments[0].scrollIntoView(true);', submit_button
        )
    submit_button.click()

except NoSuchElementException as error:
    print(
        f'Возникла ошибка:\n{error}\n'
        'Элемент по селектору не был найден на странице.'
    )

finally:
    time.sleep(20)
    browser.quit()
