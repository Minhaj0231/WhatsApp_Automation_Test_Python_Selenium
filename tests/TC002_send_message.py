import sys
sys.path.append('..')

import unittest
from  tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.message_page import MessagePage

from utils.exel.exel_helper import Excel
from utils.locators import GeneralPaths

import HtmlTestRunner

class SendMessageTest(BaseTest):

	def test_send_message(self):

		excelfile = Excel(path=GeneralPaths.exel_file_path )
		number = excelfile.get_mobile_number(row=1, col=1)

		homepage = HomePage(self.driver)
		result= homepage.go_to_message_page(number)

		if not result:
			self.assertTrue(result)

		else :
			messagePage =  MessagePage(self.driver)

			result = messagePage.send_message(number)
			

		


if __name__ == "__main__":
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= '../reports'))