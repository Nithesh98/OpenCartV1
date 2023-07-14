from selenium.webdriver.common.by import By

class LoginPage():
    txt_email_id="//input[@id='input-email']"
    txt_pwd_id="//input[@id='input-password']"
    btn_submit_xpath="//button[@type='submit']" 
    return_custmer_text="//h2[.='Returning Customer']"
    
    def __init__(self,driver):
        self.driver=driver
    
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_id).send_keys(email)
    
    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_pwd_id).send_keys(pwd)
    
    def clcikSubmit(self):
        self.driver.find_element(By.XPATH,self.btn_submit_xpath).click()

    def isReturnCustomer_Textisexists(self):
        try:
            return self.driver.find_element(By.XPATH,self.return_custmer_text).is_displayed()
        except:
            return False

    # def targetPageafterLogoin(self):
    #     self.driver.find_element()

    
    

        

