import math
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(x))))


try:
    url = 'http://suninjuly.github.io/execute_script.html'

    browser = webdriver.Chrome()
    browser.get(url)

    x = int(browser.find_element(By.ID, 'input_value').text)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(calc(x))

    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()

    robots_rule_rb = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    browser.execute_script(
            'return arguments[0].scrollIntoView(true);', robots_rule_rb
        )
    robots_rule_rb.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', button
    )
    button.click()

except NoSuchElementException as error:
    print(
        f'Возникла ошибка:\n{error}\n'
        'Элемент по селектору не был найден на странице.'
    )

finally:
    time.sleep(10)
    browser.quit()
