import sys
sys.path.append('..')

import unittest
from  tests.base_test import BaseTest
from pages.home_page import HomePage

import HtmlTestRunner


class LogOutTest(BaseTest):

		   
	def test_search_number (self):

		page = HomePage(self.driver)
		result = page.log_out()

		self.assertTrue(result)


if __name__ == "__main__":
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= '../reports'))
