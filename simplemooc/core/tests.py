from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

# Create your tests here.

class HomeViewTest(TestCase):

	def test_home_status_code(self):
		client = Client()
		respose = client.get(reverse('core:home'))
		self.assertEqual(respose.status_code, 200)

	def test_home_template_used(self):
		client = Client()
		respose = client.get(reverse('core:home'))
		self.assertTemplateUsed(respose, 'home.html')
		self.assertTemplateUsed(respose, 'base.html')

