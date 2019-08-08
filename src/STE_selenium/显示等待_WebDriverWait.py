# utf-8

# driver : 浏览器驱动
# timeout : 最长超时时间，默认以秒为单位
# poll_frequency : 检测的间隔（步长）时间，默认为0.5s
# ignored_exceptions : 超时后的异常信息，默认情况下抛NoSuchElementException异常
# WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明
# until(method,message='') : 调用该方法提供的驱动程序作为一个参数，直到返回值为True
# until_not(method,message='') : 调用该方法提供的驱动程序作为一个参数，直到返回值为false

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print('aa')
time.sleep(3)

element = WebDriverWait(driver , 5 , 0.5).until(
    EC.presence_of_element_located((By.ID , "kw"))
    )
print('456')
time.sleep(3)

element.send_keys('selenium')
time.sleep(3)


driver.quit()
