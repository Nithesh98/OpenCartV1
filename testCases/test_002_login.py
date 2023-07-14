
import pytest
# from pageObjects.AccountRegistrationPage import 
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen

import os

class Test_Login():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()  #logger
    user=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("*******Starting test_002_login **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()


        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clcikSubmit()
        
        #self.driver.close()
        self.logger.info("********End of test__002_login ******")
        #self.driver.close()

        







        
        
        