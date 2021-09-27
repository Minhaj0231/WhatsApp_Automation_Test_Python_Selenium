import sys
sys.path.append('..')

from pages.base_page import  BasePage

from utils.locators import * 
import time 

class MessagePage(BasePage):
    def __init__(self, driver):

        self.locator = MessagePageLocators
        super().__init__(driver)

    def send_message(self, number):

       
        try:
            self.find_element(*self.locator.MESSAGE_SEND_FIELD).send_keys("Test message")
            self.find_element(*self.locator.MESSAGE_SEND_BUTTON).click()
            return True
        except: 
            return False

    def check_successfully_msg_sent(self, number):

        try:
            self.find_element(*self.locator.MESSAGE_SUCCESSFULLY_SEND)
            return True
        except:
            return False
    
    def check_seen_msg(self, number):
        try:
            self.find_element(*self.locator.MESSAGE_SEEN)
            return True
        except:
            return False