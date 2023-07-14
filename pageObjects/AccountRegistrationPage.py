from selenium.webdriver.common.by import By


class AccountRegistrationPage():

    txt_firstname_cssid = "#input-firstname"
    txt_last_cssid = "#input-lastname"
    txt_email_cssid = "#input-email"
    #txt_telephone_name = ""
    txt_password_id = "#input-password"
    #txt_confpassword_name =  ""
    chk_polijcy_xpath = "//input[@type='checkbox']"
    btn_cont_xpath = "//button[.='Continue']"
    text_msg_conf_css = "div[id='content'] h1"

    def __init__(self,driver):
        self.driver=driver

    def setFirstName(self,fname):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_firstname_cssid).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_last_cssid).send_keys(lname)
    
    def setEmail(self,email):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_email_cssid).send_keys(email)

    
    def setPassword(self,pwd):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_password_id).send_keys(pwd)

    
    def setPrivacyPolicy(self):
        element=self.driver.find_element(By.XPATH,self.chk_polijcy_xpath)
        self.driver.execute_script("arguments[0].click();",element)

    def clickContinue(self):
        self.driver.execute_script("arguments[0].click();",self.driver.find_element(By.XPATH,self.btn_cont_xpath))
    

    def getconfirmations(self):
        try:
             return self.driver.find_element(By.CSS_SELECTOR,self.text_msg_conf_css).text
        except:
            None

    
    


