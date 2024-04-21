import math
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = 'http://suninjuly.github.io/get_attribute.html'

    browser = webdriver.Chrome()
    browser.get(url)

    treasure = browser.find_element(By.CSS_SELECTOR, '#treasure')
    value = treasure.get_attribute('valuex')
    y = calc(value)

    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)

    i_am_robot = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    i_am_robot.click()

    robots_rule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robots_rule.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

except NoSuchElementException as error:
    print(
        f'Возникла ошибка:\n{error}\n'
        'Элемент по селектору не был найден на странице.'
    )

finally:
    time.sleep(10)
    browser.quit()
