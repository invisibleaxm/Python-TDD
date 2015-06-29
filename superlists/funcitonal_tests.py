from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edit has heard about a cool new online to-do app. She goes to check
		# out its homepage
		self.browser.get('http://localhost:8000')

		#she notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		#she is invited to enter a to-do item straight away

		#she types "buy peackock feathers" into a text box (Edith's  hobby is tying
		#  fly-fishing lures)

		#when she hits enter, the page updates, and now the page lists "1: Buy peckonck
		# feather's" as an item in the to-do list

		#there is still a text box inviting her to add another item. She enters
		# "Use peackock feathers to make a fly"

		#The page updates again, and now shows both on her list

		#Edith wonders whether the site will remember her list Then she sees that the site
		#has generated a unique URL for her -- there is some explanatory text to that effect

		#She visits that url - her to-do list is still there

		#satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')
