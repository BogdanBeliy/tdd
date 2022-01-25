from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest


class NewVisitorTest(unittest.TestCase):
    ''' test new visitor '''

    def setUp(self):
        ''' install test '''
        self.options = Options()
        self.options.add_argument('--headless')
        self.browser = webdriver.Firefox(options=self.options)


    def test_see_main_page(self):
        ''' тест: можно начать список и получить его позже  '''

        #  Посещение главной страницы
        self.browser.get('http://127.0.0.1:8000/')
        # проверка на наличие нужного заголовка
        self.assertIn('To-do', self.browser.title, 'Failure')



if __name__ == '__main__':
    unittest.main()
