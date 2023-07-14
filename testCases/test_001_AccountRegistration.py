from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
#driver=None
import time
from utilities import randomstring
import os
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen # for logging 
import pytest
class Test_001_AccountReg:
    baseURL= ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("****test_001_Account Registration_Is _started****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("launching application")
        self.driver.maximize_window()
        self.hp=HomePage(self.driver)
        self.logger.info("clicking on My account----->Register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage=AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("john")
        self.regpage.setLastName("qa")
        self.email=randomstring.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setPassword("123456")
        # self.driver.implicitly_wait(5)
        time.sleep(5)   
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.getconfirmations()
        if self.confmsg=="Register Account":
            self.logger.info("Account Registration_Is passed")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
            self.logger.error("Account Registration_Is failed")
            self.driver.close()
            assert False
        self.logger.info("****test_001_Account Registration_Is finished****")
        
    



        


 

        










    


         