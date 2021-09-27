import sys
sys.path.append('..')

import unittest
from  tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.message_page import MessagePage

from utils.exel.exel_helper import Excel
from utils.locators import GeneralPaths
import HtmlTestRunner


class SuccessFullyMsgSent(BaseTest):

	def test_check_msg_sent(self):

		excelfile = Excel(path=GeneralPaths.exel_file_path )
		number = excelfile.get_mobile_number(row=1, col=1)

		homepage = HomePage(self.driver)
		result= homepage.go_to_message_page(number)

		if not result:
			self.assertTrue(result)

		else :
			messagePage =  MessagePage(self.driver)

			result = messagePage.check_successfully_msg_sent(number)

			excelfile.write_in_excel_sheet("sent", row=1, col=2)
		


if __name__ == "__main__":
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= '../reports'))