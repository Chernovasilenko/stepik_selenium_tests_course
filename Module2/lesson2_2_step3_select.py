import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    url = 'http://suninjuly.github.io/selects1.html'

    browser = webdriver.Chrome()
    browser.get(url)

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    answer = num1 + num2

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(answer))

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
