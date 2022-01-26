from django.test import TestCase
from django.urls import resolve #используется для поиска функции или класса соответствующей URL
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    ''' test home page '''

    def test_root_resolve_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    # def test_correct_html_home_page(self):
    #     response = self.client.get('/')
    #     self.assertTemplateUsed(response, 'home.html')
    #     print('new test func')

    def test_can_save_post(self):
        response = self.client.post('/', data={'item_text': 'Купить носки'})
        self.assertIn('Купить', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')





