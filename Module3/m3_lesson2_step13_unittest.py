import time
import unittest


from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):

    link_v1 = 'http://suninjuly.github.io/registration1.html'
    link_v2 = 'http://suninjuly.github.io/registration2.html'
    congratulation = 'Congratulations! You have successfully registered!'
    error_message = 'Текст после заполнения формы не соответствует ожидаемому.'

    @staticmethod
    def registration(link: str) -> str:
        browser = webdriver.Chrome()
        browser.get(link)

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

        browser.quit()

        return welcome_text

    def test_registration1(self):
        welcome_text = self.registration(self.link_v1)
        self.assertEqual(
            self.congratulation, welcome_text, self.error_message
        )

    def test_registration2(self):
        welcome_text = self.registration(self.link_v2)
        self.assertEqual(
            self.congratulation, welcome_text, self.error_message
        )


if __name__ == '__main__':
    unittest.main()
