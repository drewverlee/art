#!/usr/local/bin/python
import unittest
import sys
from selenium import webdriver

servers = {
        'live' : 'http://safe-sands-8472.herokuapp.com/',
        'local': 'http://127.0.0.1:5000/'
        }

class TestApp(unittest.TestCase):


    BASE = servers['local']

    @classmethod
    def setUpClass(cls):
        cls.c = webdriver.PhantomJS()

    def setUp(self):
        self.c.get(self.BASE)

    def tearDown(self):
        self.c.quit()

    def test_home_page(self):
        self.assertEqual('Home', self.c.title)
        self.assertEqual('DrewsArt', self.c.find_element_by_id('banner').text)
        

if __name__ == '__main__':
    if len(sys.argv) > 1: TestApp.BASE = servers[sys.argv.pop()]
    unittest.main()

