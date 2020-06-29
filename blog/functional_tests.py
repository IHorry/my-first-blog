from selenium import webdriver
import unittest

"""
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title, "Browser Title was " + browser.title

"""
class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Chrome()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Django', self.browser.title)  


        

if __name__ == '__main__':  
    unittest.main(warnings='ignore')