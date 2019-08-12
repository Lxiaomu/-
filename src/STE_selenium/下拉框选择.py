# utf-8

# 例：百度搜索设置的下拉框

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 鼠标悬停至设置链接
driver.find_element_by_link_text("设置").click()
print('找到设置按钮并点击')
sleep(2)

# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
print('打开搜索设置并点击')
sleep(2)

# 搜索结果显示条数
sel = driver.find_element_by_xpath("//select[@id = 'nr']")
print('定位')
sleep(2)
# Select类用于定位select标签
# select_by_value() 方法用于定位下接选项中的value值。
Select(sel).select_by_value('50')   # 显示50条
#......


driver.quit()
