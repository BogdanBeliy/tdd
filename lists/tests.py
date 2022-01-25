from django.test import TestCase
from django.urls import resolve #используется для поиска функции или класса соответствующей URL
from lists.views import home_page
from django.http import HttpRequest


class HomePageTest(TestCase):
    ''' test home page '''


    def test_root_resolve_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        print('func done')


    def test_html_home_page(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-do</title>', html)
        self.assertTrue(html.endswith('</html>'))
        print('html done')



