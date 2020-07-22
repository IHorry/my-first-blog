from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase
from blog.views import *
from blog.models import CV,Skill,Work,Qual


# Create your tests here.
class ConfigTest(TestCase):

    def test_testing(self):
        self.assertEqual(1 + 1, 2)


    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list)


    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        print(html)  



class CVTesting(TestCase):

	def test_super_header_displayed(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		self.assertIn("Isaac Horry",html)

	def test_CV_section_allocated(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		self.assertIn('<div class="CV_container"',html)

	


	def test_CV_model(self):
		new_CV = CV()
		new_CV.summary = 'This is a quick summary of my CV'
		new_CV.save()

		saved_items = CV.objects.all()

		self.assertEqual(saved_items.count(),1)
		self.assertEqual(CV.objects.first().summary,'This is a quick summary of my CV')

		new_CV.summary = 'This is a quick summary of my CV-edited'
		self.assertEqual(CV.objects.first().summary,'This is a quick summary of my CV-edited')


	def test_work_model(self):
		new_workExp =Work()
		new_workExp.title = 'Cleaner'
		new_workExp.id_company = 'Janitorial Services'
		new_workExp.dateStarted = '1999-09-23'
		new_workExp.dateEnd = '2001-09-23'
		new_workExp.save()

		saved_items = Work.objects.all()

		self.assertEqual(saved_items.count(),1)
		self.assertEqual(Work.objects.first().title,'Cleaner')

		new_workExp.title = 'Cleaner-edited'
		new_workExp.save()
		self.assertEqual(Work.objects.first().title,'Cleaner-edited')



	def test_qual_model(self):
		new_qual = Qual()
		new_qual.qualification = 'GCSE'
		new_qual.subject = 'Maths'
		new_qual.grade = 'C'

		new_qual.save()

		saved_items = Qual.objects.all()

		self.assertEqual(saved_items.count(),1)
		self.assertEqual(Qual.objects.first().grade,'C')



		new_qual.grade = 'A'
		new_qual.save()
		self.assertEqual(Qual.objects.first().grade,'A')



	def test_skills_model(self):
		new_skill = Skill()
		new_skill.skill = 'Croquet'
		new_skill.description = 'A very posh game'
		new_skill.save()

		saved_items = Skill.objects.all()

		self.assertEqual(saved_items.count(),1)
		self.assertEqual(Skill.objects.first().description,'A very posh game')

		new_skill.skill = 'Polo'
		new_skill.save()
		self.assertEqual(Skill.objects.first().skill,'Polo')


	def test_CV_snippet_displayed(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		self.assertIn("summary",html)


	def obselete_test_CV_can_create(self):
		response = self.client.get('/')

		html = response.content.decode('utf8')
		self.assertIn('Add New CV',html)



	def test_cv_make_changes_not_logged_in(self):
		response = self.client.get('/')

		html = response.content.decode('utf8')
		self.assertNotIn('CV_edit',html)


	def test_view_full_cv(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		self.assertIn('summary',html)
		self.assertIn('Skills and Experience',html)
		self.assertIn('Qualifications and Education',html)
		self.assertIn('Previous Work Experience',html)
		self.assertIn('Interests',html)








		
		















		

        


