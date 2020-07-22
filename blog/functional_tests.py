from selenium import webdriver
import unittest
import time
from django.urls import resolve
from django.test import TestCase


"""
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title, "Browser Title was " + browser.title

"""
#classes reference the type of user: Visitor or Admin
#deals with all the actions that can performed by a visitor
class VisitorTests(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Chrome()

    def tearDown(self):  
        self.browser.quit()

    def test_functest(self):  
        self.browser.get('http://localhost:8000')

        self.assertIn('Django', self.browser.title)  


    def test_view_CV(self):

        self.browser.get('http://localhost:8000')


        view_full_button = self.browser.find_element_by_id('CV_viewfull')
        view_full_button.click()
        time.sleep(1)
        self.assertEqual(view_full_button.get_attribute('innerHTML'),'Close')



class AdminCVTests(unittest.TestCase):

    def setUp(self):  
        self.browser = webdriver.Chrome()
        self.login()
        
    def login(self):
        self.browser.get('http://localhost:8000/accounts/login')
        print(self.browser.current_url)
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys("ihorry")
        password.send_keys("hinges123")
        submit = self.browser.find_element_by_id('id_submit')
        submit.click()
        time.sleep(2)
        self.assertEqual(self.browser.current_url,'http://localhost:8000/')


    def tearDown(self):  
        self.browser.quit()


    def obselete_test_move_to_newcv_page(self):
        self.browser.get('http://localhost:8000/')
        plus = self.browser.find_element_by_id('CV_placeholder')
        plus.click()
        self.assertEqual(self.browser.current_url,'http://localhost:8000/cv/new/')


    def test_edit_summary(self):

        self.browser.get('http://localhost:8000/cv/edit')
        time.sleep(2)
        summary_div = self.browser.find_element_by_class_name('summary-div')
        summary = summary_div.find_element_by_tag_name('textarea')

        summary.clear()
        summary.send_keys("Just a quick summary of my cv")
        summary.submit()




        self.assertEqual(self.browser.current_url,'http://localhost:8000/')
        summary_div = self.browser.find_element_by_id('summary-div1')
        summary = summary_div.find_element_by_tag_name('p')

        self.assertEqual(summary.get_attribute('innerHTML'),"Just a quick summary of my cv")


    def test_edit_references(self):

        self.browser.get('http://localhost:8000/cv/edit')
        references_div = self.browser.find_element_by_class_name('references-div')
        references = references_div.find_element_by_tag_name('textarea')
        references.clear()
        references.send_keys("references")

        references.submit()


        self.assertEqual(self.browser.current_url,'http://localhost:8000/')
        view_full_button = self.browser.find_element_by_id('CV_viewfull')
        view_full_button.click()
        time.sleep(2)
        references_div = self.browser.find_element_by_class_name('references-div')
        references = references_div.find_element_by_tag_name('p')
        self.assertEqual(references.get_attribute('innerHTML'),"references ")

        



    def test_edit_interests(self):

        
        self.browser.get('http://localhost:8000/cv/edit')
        interests_div = self.browser.find_element_by_class_name('interests-div')
        interests = interests_div.find_element_by_tag_name('textarea')
        interests.clear()
        interests.send_keys("interests")

        interests.submit()

        self.assertEqual(self.browser.current_url,'http://localhost:8000/')
        view_full_button = self.browser.find_element_by_id('CV_viewfull')
        view_full_button.click()
        time.sleep(2)
        interests_div = self.browser.find_element_by_class_name('interests-div')
        interests = interests_div.find_element_by_tag_name('p')
        self.assertEqual(interests.get_attribute('innerHTML'),"interestsl")


    def test_new_workExp(self):
        self.browser.get('http://localhost:8000/cv/edit')
        time.sleep(2)
        workExp = self.browser.find_element_by_xpath("//a[@id='id_workExp']").click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url,'http://localhost:8000/cv/edit/work/new')

    
    def test_new_qual(self):
        self.browser.get('http://localhost:8000/cv/edit')
        time.sleep(2)
        qual = self.browser.find_element_by_xpath("//a[@id='id_qual']").click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url,'http://localhost:8000/cv/edit/qual/new')


    def test_new_skills(self):
        self.browser.get('http://localhost:8000/cv/edit')
        time.sleep(2)
        skills = self.browser.find_element_by_xpath("//a[@id='id_skills']").click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url,'http://localhost:8000/cv/edit/skill/new')



if __name__ == '__main__':  
    unittest.main(warnings='ignore')