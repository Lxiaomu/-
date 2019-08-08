# utf-8
# perform():执行所有ActionChains中存储的行为。
# context.click(): 右击
# double.click(): 双击
# drag_and_drop(): 拖动
# move_to_element(): 鼠标暂停


#鼠标悬停操作
import time
from selenium import webdriver
#导入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#定位到要悬停的元素
above = driver.find_element_by_link_text("设置")
#对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()

