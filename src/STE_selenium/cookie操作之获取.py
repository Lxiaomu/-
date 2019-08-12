# utf-8
"""
WebDriver提供了操作Cookie的相关方法，可以读取、添加和删除cookie信息
WebDriver操作cookie的方法：
 get_cookies()： 获得所有cookie信息
 get_cookie(name)： 返回字典的key为“name”的cookie信息
 add_cookie(cookie_dict) ： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值
 delete_cookie(name,optionsString)：删除cookie信息
 “name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。
 delete_all_cookies()： 删除所有cookie信息
"""
# 通过get_cookies()来获取当前浏览器的cookie信息

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")
print('开始')
time.sleep(2)


# 获得cookie信息
cookie= driver.get_cookies()
print('获取')
time.sleep(2)
# 将获得cookie的信息打印
print(cookie)
time.sleep(2)

driver.quit()
