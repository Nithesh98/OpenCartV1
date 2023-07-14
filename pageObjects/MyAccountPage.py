from selenium.webdriver.common.by import By

class MyAccountPage():
    lnk_logout_xcpath=""

    def __init__(self,driver):
        self.driver=driver

    def clcikLogout(self):
        self.driver.find_element(By.XPATH,self.lnk_logout_xcpath).click()