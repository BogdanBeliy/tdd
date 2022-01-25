from django.test import TestCase



class SmokeTest(TestCase):
    ''' test by tocsick '''

    def test_bad_maths(self):
        self.assertEqual(1+1,3)

