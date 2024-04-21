import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


try:
    url = 'http://suninjuly.github.io/file_input.html'

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    browser = webdriver.Chrome()
    browser.get(url)

    f_name_input = browser.find_element(By.NAME, 'firstname')
    f_name_input.send_keys('Ivan')

    l_name_input = browser.find_element(By.NAME, 'lastname')
    l_name_input.send_keys('Ivanov')

    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('i.ivanov@stepik.org')

    file_input = browser.find_element(By.ID, 'file')
    file_input.send_keys(file_path)

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
