import sys
sys.path.append('..')

import unittest
from  tests.base_test import BaseTest
from pages.home_page import HomePage

from utils.exel.exel_helper import Excel
from utils.locators import GeneralPaths

import HtmlTestRunner

class SearchTest(BaseTest):

		   
	def test_search_number (self):

		excelfile = Excel(path=GeneralPaths.exel_file_path )
		number = excelfile.get_mobile_number(row=1, col=1)
		page = HomePage(self.driver)
		
		result =  page.search_number(number)
		

		self.assertTrue(result)
		

if __name__ == "__main__":
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= '../reports'))


