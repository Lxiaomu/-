#  utf-8

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print("adf")     #打印
time.sleep(3)


#找到输入框并输入
abc = driver.find_element_by_id("kw")
print("123")
time.sleep(2)
abc.send_keys("小白")  #输入值
print("bbb")
time.sleep(3)

#清除文本数据
driver.find_element_by_id("kw").clear()
print("aaa")
time.sleep(3)

#找到输入框并输入值
abc = driver.find_element_by_id("kw")
print("123")
time.sleep(2)
abc.send_keys("selenium")
print("bbb")
time.sleep(3)

abc.submit()   #模拟回车键

#点击百度按钮元素
#driver.find_element_by_id("su").click()
#print("ccc")

time.sleep(4)
driver.quit()   #彻底退出关闭网页
