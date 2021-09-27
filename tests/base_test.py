import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils.locators import GeneralPaths, XPaths

class BaseTest(unittest.TestCase):

    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(GeneralPaths.website_path)

        while True:
            try:
                self.driver.find_element_by_xpath(XPaths.captcha_solved_check_xpath) 

                break
            except:
                None

        
             

    def tearDown(self):
        self.driver.close()


   
