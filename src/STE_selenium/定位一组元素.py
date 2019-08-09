#  utf-8
# 定位一组元素与定位单个元素的方法类似，区别在于单词element后面多了s表示复数
# find_elements_by_id()
# find_elements_by_name()
# find_elements_by_class_name()
# find_elements_by_tag_name()
# find_elements_by_link_text()
# find_elements_by_partial_link_text()
# find_elements_by_xpath()
# find_elements_by_css_selector()


from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print("开始")
sleep(2)

driver.find_element_by_id("kw").send_keys("selenium")
print('11')
driver.find_element_by_id("su").click()
print('22')
sleep(2)

#定位一组元素
texts = driver.find_elements_by_xpath('//div/h3/a')
print(texts)
sleep(2)

#循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)
sleep(3)


driver.quit()







