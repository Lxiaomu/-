# utf-8

# title ：用于获得当前页面的标题
# current_url ：用于获得当前页面的URL
# text ：获取搜索条目的文本信息




from selenium import webdriver
from time import sleep          #  类似 import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print("aa")
sleep(2)


# 打印当前页面title
title = driver.title
print(title)
sleep(2)

#打印当前页面URL
now_url = driver.current_url
print(now_url)
sleep(2)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)
print('22')

#再次打印当前页面title
title = driver.title
print(title)

#打印当前页面URL
now_url = driver.current_url
print(now_url)
sleep(2)

#获取结果数目
user = driver.find_element_by_class_name('nums').text
print(user)
sleep(2)

driver.quit()




