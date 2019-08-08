# utf-8
# size: 返回元素的尺寸
# text: 获取元素的文本
# get_attribute(name): 获取属性值
# is_displayed(): 设置该元素是否用户可见


import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#获得输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)
time.sleep(2)

#返回百度页面底部备案信息
text = driver.find_element_by_id('cp').text
print(text)
time.sleep(2)

#返回元素的属性值，可以是id, name . type 或者其他任意属性
attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)
time.sleep(2)

#返回元素的结果是否可见，返回结果为true 或者 false
result = driver.find_element_by_id('kw').is_displayed()
print(result)
time.sleep(3)

driver.quit()
