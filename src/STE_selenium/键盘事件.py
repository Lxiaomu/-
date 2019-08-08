# utf-8

# send_keys(Keys.BACK_SPACE)   删除键（BackSpace）
# send_keys(Keys.SPACE)        空格键（Space）
# send_keys(Keys.TAB)          制表键（Tab）
# send_keys(Keys.ESCAPE)       回退键（Esc）
# send_keys(Keys.ENTER)        回车键（Enter）
# send_keys(Keys.CONTROL,'a')  全选（Ctrl+A）
# send_keys(Keys.CONTROL,'c')  复制（Ctrl+C）
# send_keys(Keys.CONTROL,'x')  剪切（Ctrl+X）
# send_keys(Keys.CONTROL,'v')  粘贴（Ctrl+V）
# send_keys(Keys.F1)           键盘F1
# .....
# send_keys(Keys.F12)          键盘F12



import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys    #引入 Keys模块


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(2)
print('11')

#输入框输入内容
driver.find_element_by_id('kw').send_keys("selenium好")
print('22')
time.sleep(2)


#删除多输入的一个 好
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
print('33')
time.sleep(2)

#输入空格键+“教程”
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
print('44')
time.sleep(2)
driver.find_element_by_id('kw').send_keys("教程")
print('44')
time.sleep(2)

#ctrl+a 全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
print('55')
time.sleep(2)

#ctrl+a 剪切输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
print('66')
time.sleep(2)

#ctrl+a 粘贴输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
print('77')
time.sleep(2)


#通过回车键代替单击操作
driver.find_element_by_id('su').send_keys(Keys.ENTER)
print('88')
time.sleep(2)
driver.quit()



