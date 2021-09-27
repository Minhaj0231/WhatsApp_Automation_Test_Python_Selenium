from selenium.webdriver.common.by import By


class HomePageLocators(object):


    SEARCH = (By.CSS_SELECTOR, '#side > div.uwk68 > div > label > div > div._13NKt.copyable-text.selectable-text')
    SEARCH_RESULT =  (By.CSS_SELECTOR, '#pane-side > div:nth-child(1) > div > div > div:nth-child(5) > div')
    SEARCHED_USER = (By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[4]' )

    LOGOUT_MENU = (By.CSS_SELECTOR, '#side > header > div._3yZPA > div > span > div:nth-child(3) > div > span')
    
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#side > header > div._3yZPA > div > span > div._2cNrC._1CTfw > span > div.o--vV.wGJyi > ul > li:nth-child(6)')

class MessagePageLocators(object):

    MESSAGE_SEND_FIELD = (By.CSS_SELECTOR, '#main > footer > div._2BU3P.tm2tP.copyable-area > div > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text' )    
    MESSAGE_SEND_BUTTON = ( By.CSS_SELECTOR, '#main > footer > div._2BU3P.tm2tP.copyable-area > div > div > div._2lMWa > div._3HQNh._1Ae7k > button')
    MESSAGE_SUCCESSFULLY_SEND = ( By.CSS_SELECTOR , '#main > div._1LcQK > div > div._33LGR > div.y8WcF > div:nth-child(24) > div > div > div > div._1beEj > div > div > span > svg')
    MESSAGE_SEEN = ( By.CSS_SELECTOR , '#main > div._1LcQK > div > div._33LGR > div.y8WcF > div:nth-child(21) > div > div > div > div._1beEj > div > div > span > svg')



class XPaths(object):

    captcha_solved_check_xpath = '//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[1]' # a random component's xpath of homepage after the captcha is solved 


class GeneralPaths(object):

    website_path = "https://web.whatsapp.com/"

    exel_file_path = ""  # Todo enter exel file path 




