# utf-8

"""在WebDriver中处理JavaScript所生成的alert、confirm以及prompt十分简单，
具体做法是使用 switch_to.alert 方法定位到 alert/confirm/prompt，
然后使用text/accept/dismiss/ send_keys等方法进行操作:
text：返回 alert/confirm/prompt 中的文字信息
accept()：接受现有警告框
dismiss()：解散现有警告框
send_keys(keysToSend)：发送文本至警告框。keysToSend：将文本发送至警告框

"""
# 百度搜索设置弹出的窗口是不能通过前端工具对其进行定位的，这个时候就可以通过switch_to_alert()方法接受这个弹窗

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
print('开始')
time.sleep(2)

# 鼠标悬停至“设置”链接
link = driver.find_element_by_link_text('设置')
print('找到设置')
time.sleep(2)
ActionChains(driver).move_to_element(link).perform()
print('鼠标悬停')
time.sleep(2)

# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
print('找到搜索设置并点击')
time.sleep(2)

# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()
print('保存设置')
time.sleep(2)

# 接受警告框
driver.switch_to.alert.accept()
print('接受')
time.sleep(2)


driver.quit()
