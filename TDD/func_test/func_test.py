from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    ''' test new visitor '''

    def setUp(self):
        ''' install test '''
        # self.options = Options()
        # self.options.add_argument('--headless')
        self.browser = webdriver.Firefox()


    def test_see_main_page(self):
        ''' тест: можно начать список и получить его позже  '''

        #  Посещение главной страницы
        self.browser.get('http://127.0.0.1:8000/')
        # проверка на наличие нужного заголовка
        self.assertIn('To-do', self.browser.title, 'Failure')
        # find headertext h1
        header_text = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-do', header_text.text)
        # send word in input
        input_box = self.browser.find_element_by_id('new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter to-do item')
        input_box.send_keys('Оплатить')
        time.sleep(2)
        input_box.send_keys(Keys.ENTER)
        time.sleep(10)
        table = self.browser.find_element_by_id('list_item')
        self.assertIn('Оплатить', [row.text for row in table.find_elements_by_tag_name('tr')])


    def tearDown(self):
        self.browser.close()
        print('test is finish')







if __name__ == '__main__':
    unittest.main()
