#獨立測試案例, 每個def 都是一個獨立的案例需要重新建立session
import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from BeautifulReport import BeautifulReport
from settings import session
import settings


current_path = os.getcwd()
report = os.path.join(current_path, "Report")
now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))

report_title = settings.Product_flag + "_" + now + ".html"
des = "獨立測試案例"

#product_list = ["Qvideo","Qget"]
#loop_times = 1
#Product_flag = "Qget"

class Login(unittest.TestCase):
    #@classmethod
    def setUp(self):
        print("start")
        if settings.Product_flag == "Qvideo":
            session.setsession_Qvideo(self)
        elif settings.Product_flag == "Qget":
            session.setsession_Qget(self)
    """
    def test_LANlogin_SSLOFF(self):
        '''LAN login'''
        settings.login(self, IP_or_Host = "10.20.241.197",AC = "admin", PWD = "@dmin1234", SSL = "disable",
                       AutoPort = "enable", Lanport = "8080")
    def test_LANlogin_SSLON(self):
        '''LAN login'''
        settings.login(self, IP_or_Host = "10.20.241.197",AC = "admin", PWD = "@dmin1234", SSL = "enable",
                       AutoPort = "enable", Lanport = "8080")
    """
    def test_WANlogin_SSLOFF(self):
        '''WAN login'''
        settings.login(self, IP_or_Host = "115.43.107.17", AC = "cindy", PWD = "cindy", SSL = "disable",
                       AutoPort = "disable", Lanport = "5000")
    def test_WANlogin_SSLON(self):
        '''WAN login'''
        settings.login(self, IP_or_Host = "115.43.107.17", AC = "cindy", PWD = "cindy", SSL = "enable",
                       AutoPort = "disable", Lanport = "5001")

        #yy1 = yy.d1(self)
        #yy1 = yy.d2(self)
    """
    def test_myQNAPcloud_login(self):
        '''myQNAPcloud login'''
        settings.login(self, IP_or_Host = "mingjehouse.myqnapcloud.com",AC = "cindy", PWD = "cindy", SSL = "disable",
                       AutoPort = "enable", Lanport = "5001")

    def test_cloudlink_login(self):
        '''Cloudlink login'''
        self.driver.find_element_by_xpath("xpath=//*[@id='btn_right']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='addServer']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='IDTV_MANUAL']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='server_host_edit']").send_keys(settings.NAS1.cloudlnk)
        self.driver.find_element_by_xpath("xpath=//*[@id='user_name_edit']").send_keys(settings.NAS1.ac)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='user_password_edit']")))
        self.driver.find_element_by_xpath("xpath=//*[@id='user_password_edit']").send_keys(settings.NAS1.pwd)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='server_edit_done']")))
        self.driver.find_element_by_xpath("xpath=//*[@id='server_edit_done']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='button1']")))
        self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='drawer opened']").click()
        self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']")
        flag = self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']").text
        assert flag == "CloudLink"
    """
    def test_minus(self):
        print("5")
    #@classmethod
    def tearDown(self):
        print("close")
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    #tests = ["test_minus1", "test_uu", "test_add", "test_mul", "test_minus"]
    for i in range(settings.loop_times):
        suite.addTests(unittest.makeSuite(Login))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(yu))
    #suite = unittest.TestSuite(map(yu, tests))

    # suite.addTests(suite1)
    print(suite)
    result = BeautifulReport(suite)
    result.report(description=des, filename=report_title, log_path=report)
