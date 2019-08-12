# utf-8

# <!-- window.scrollTo(左边距，上边距)
# window.scrollTo(0,450)
# WebDriver提供了execute_script()方法来执行JavaScript代码
# set_window_size()方法将浏览器窗口设置为固定宽高显示，目的是让窗口出现水平和垂直滚动条
# 然后通过execute_script()方法执行JavaScripts代码来移动滚动条的位置



from selenium import webdriver
from time import sleep

# 访问百度
driver = webdriver.Chrome()
driver.get("http://baidu.com")
print("进入百度页面")

# 设置浏览器窗口大小
driver.set_window_size(500,500)
print('设置窗口大小')
sleep(2)

# 搜索
driver.find_element_by_id('kw').send_keys("selenium")
print("找到输入框并输入值selenium")
sleep(2)
driver.find_element_by_id('su').click()
print("找到搜索按钮并点击")
sleep(2)

# 通过JavaScipt设置浏览器窗口的滚动位置
js = "window.scrollTO(400,450)"
print('设置')
sleep(2)
driver.execute_script(js)
print('提交代码')
sleep(3)


driver.quit()
