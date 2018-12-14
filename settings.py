import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from appium import webdriver

from selenium.common.exceptions import NoSuchElementException


#cmd = 'python tt9.py'
#os.system(cmd)
Product_flag = "Qvideo"
loop_times = 1


class session:

    def setsession_Qvideo(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["platformVersion"] = "5.1.1"
        self.dc["deviceName"] = "7537c434"
        self.dc["appPackage"] = "com.qnap.qvideo"
        self.dc["appActivity"] = ".Qvideo"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        #self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def setsession_Qget(self):
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["platformVersion"] = "5.1.1"
        self.dc["deviceName"] = "7537c434"
        self.dc["appPackage"] = "com.qnap.com.qgetpro"
        self.dc["appActivity"] = ".Splash"
        # desired_caps["appActivity"] = ".login.LoginActivity"
        #self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)


class profile:
    def __init__(self, n, lanip1, lanip2, wanip, myDDNS, cloudlink, lanport, ac, pwd):
        self.name = n
        self.NASLANIP1 = lanip1
        self.NASLANIP2 = lanip2
        self.WANIP = wanip
        self.myDDNS = myDDNS
        self.cloudlnk = cloudlink
        self.lanport = lanport
        self.ac = ac
        self.pwd = pwd

NAS1 = profile("TVS-473", "192.168.79.200", "10.20.241.197", "115.43.107.17", "steventvs473.myqnapcloud.com",
                   "steventvs473", "8080", "admin", "@dmin1234")
NAS2 = profile("TVS-473", "192.168.79.200", "10.20.241.197", "115.43.107.17", "mingjehouse.myqnapcloud.com",
                   "mingjehouse", "5001", "cindy", "cindy")

def login(self, IP_or_Host = NAS1.NASLANIP2, AC = NAS1.ac, PWD = NAS1.pwd, SSL = "disable", AutoPort = "enable",
          Lanport = NAS1.lanport):
    '''這是失敗的用例'''
    try:
        self.driver.find_element_by_xpath("xpath=//*[@id='qbu_tvStart']").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@class='android.widget.ImageButton']")))
        self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.ImageButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='IDTV_MANUAL']").click()

    except NoSuchElementException:
        try:
            self.driver.find_element_by_xpath("xpath=//*[@id='btn_right']").click()
        except NoSuchElementException:
            pass
        self.driver.find_element_by_xpath("xpath=//*[@id='addServer']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='IDTV_MANUAL']").click()

    self.driver.find_element_by_xpath("xpath=//*[@id='server_host_edit']").send_keys(IP_or_Host)
    self.driver.find_element_by_xpath("xpath=//*[@id='user_name_edit']").send_keys(AC)
    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='user_password_edit']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='user_password_edit']").send_keys(PWD)
    if SSL == "disable":
        pass
    else:
        self.driver.find_element_by_xpath("//*[@id='safe_connection_checkbox']").click()

    if AutoPort == "enable":
        pass
    else:
        self.driver.find_element_by_xpath("xpath=//*[@id='button_goto_advanced']").click()
        self.driver.swipe(669, 748, 672, 563, 503)
        self.driver.swipe(621, 603, 615, 324, 352)
        self.driver.find_element_by_xpath("xpath=//*[@id='autoport_checkbox']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='port_simple']").send_keys(Lanport)
    WebDriverWait(self.driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@class='android.support.v7.widget.LinearLayoutCompat']")))
    self.driver.find_element_by_xpath("xpath=//*[@class='android.support.v7.widget.LinearLayoutCompat']").click()
    time.sleep(5)
    try:
        self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
    except NoSuchElementException:
        pass
    time.sleep(5)
    self.driver.find_element_by_xpath("xpath=//*[@contentDescription='drawer opened']").click()
    self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']")
    flag = self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']").text
    assert flag == IP_or_Host


def LAN_login(self):

    self.driver.find_element_by_xpath("xpath=//*[@id='btn_right']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='addServer']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='IDTV_MANUAL']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='server_host_edit']").send_keys(NAS1.NASLANIP2)
    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='user_password_edit']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='user_password_edit']").send_keys(NAS1.pwd)
    # WebDriverWait(self.driver, 10).until(
    # expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='server_edit_done']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='server_edit_done']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
    time.sleep(2)
    self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
    time.sleep(5)
    self.driver.find_element_by_xpath("xpath=//*[@contentDescription='drawer opened']").click()
    self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']")
    flag = self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']").text
    assert flag == NAS1.NASLANIP2

def WAN_login(self):
    self.driver.find_element_by_xpath("xpath=//*[@id='btn_right']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='addServer']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='IDTV_MANUAL']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='server_host_edit']").send_keys(NAS2.WANIP)
    self.driver.find_element_by_xpath("xpath=//*[@id='user_name_edit']").send_keys(NAS2.ac)
    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='user_password_edit']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='user_password_edit']").send_keys(NAS2.pwd)
    self.driver.find_element_by_xpath("xpath=//*[@id='button_goto_advanced']").click()
    self.driver.swipe(669, 748, 672, 563, 503)
    self.driver.swipe(621, 603, 615, 324, 352)
    self.driver.find_element_by_xpath("//*[@id='safe_connection_checkbox']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='autoport_checkbox']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='port_simple']").send_keys(NAS2.lanport)
    WebDriverWait(self.driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='server_edit_done']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='server_edit_done']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
    time.sleep(5)
    self.driver.find_element_by_xpath("xpath=//*[@contentDescription='drawer opened']").click()
    self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']")
    flag = self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']").text
    assert flag == NAS2.WANIP


def myQNAPcloud_login(self):
    '''這是失敗的用例'''
    self.driver.find_element_by_xpath("xpath=//*[@id='addServer']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='IDTV_MANUAL']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='server_host_edit']").send_keys(NAS2.myDDNS)
    self.driver.find_element_by_xpath("xpath=//*[@id='user_name_edit']").send_keys(NAS2.ac)
    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='user_password_edit']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='user_password_edit']").send_keys(NAS2.pwd)
    WebDriverWait(self.driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='server_edit_done']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='server_edit_done']").click()
    time.sleep(5)
    self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
    time.sleep(5)
    self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()
    time.sleep(5)
    self.driver.find_element_by_xpath("xpath=//*[@contentDescription='drawer opened']").click()
    self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']")
    flag = self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']").text
    assert flag == NAS2.myDDNS



def Regionset(self, Region):
    if Region == "Globalset":
        #driver.find_element_by_xpath("xpath=//*[@id='btn_right']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='setting']").click()
        self.driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout' and @index='8']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='region_name']").click()
        try:
            self.driver.find_element_by_xpath("xpath=//*[@id='text1'][@index='0'][@checked='true']")
            self.driver.find_element_by_xpath("xpath=//*[@id='button2']").click()
        except:
            self.driver.find_element_by_xpath("xpath=//*[@id='text1' and @index='0']").click()

    elif Region == "Chinaset":
        self.driver.find_element_by_xpath("xpath=//*[@id='setting']").click()
        self.driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout' and @index='8']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='region_name']").click()
        try:
            self.driver.find_element_by_xpath("xpath=//*[@id='text1'][@index='1'][@checked='true']")
            self.driver.find_element_by_xpath("xpath=//*[@id='button2']").click()
        except:
            self.driver.find_element_by_xpath("xpath=//*[@id='text1' and @index='1']").click()









