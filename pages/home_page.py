import sys
sys.path.append('..')

from pages.base_page import  BasePage

from utils.locators import * 
import time 

class HomePage(BasePage):
    def __init__(self, driver):

        self.locator = HomePageLocators

        super().__init__(driver)



    def search_number(self, number ):
        self.find_element(*self.locator.SEARCH).send_keys(number) 

        time.sleep(3) # waiting  few seconds for data loding 

        try:
            self.find_element(*self.locator.SEARCH_RESULT)
            return True
        except:
             return False 


    def go_to_message_page(self, number):

        valid_number = self.search_number(number)

        if not valid_number :
            return False 

        self.find_element(*self.locator.SEARCHED_USER).click()

        time.sleep(3) # waiting  few seconds for data loding 

        return True 

   
    def log_out(self):

        try:
            
            self.find_element(*self.locator.LOGOUT_MENU).click()
            
            time.sleep(3)  # waiting  few seconds for data loding 


            self.find_element(*self.locator.LOGOUT_BUTTON).click()
            return True

        except: 
            return False


        

        