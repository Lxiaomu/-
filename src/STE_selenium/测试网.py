# utf-8

from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("http://www.testclass.net")
print('进入测试网')
sleep(1)
driver.maximize_window()
print('浏览器最大化')
sleep(1)


driver.find_element_by_xpath("//*[@href = '/readers/sign_in']").click()
print('找到用户登录并点击')
sleep(1)

driver.find_element_by_id('reader_email').send_keys('1106361798@qq.com')
print('输入电子邮箱')
sleep(1)

driver.find_element_by_id('reader_password').send_keys('a1106361798')
print('输入密码')
sleep(1)

driver.find_element_by_name('commit').click()
print('点击登录按钮')
sleep(2)

driver.find_element_by_xpath("//*[@href = '/selenium_python']").click()
print('点击选择文章 selenium python')
sleep(2)

driver.find_element_by_xpath("//*[@href = '/selenium_python/qa']").click()
print("点击选择进入小结<常见问题>")
sleep(2)

driver.find_element_by_id('comment_content').send_keys('利用空闲时间终于学完了这二十个章节，虽然目前还只学会一点点基础，但真的受益很大，感谢虫师')
print('评论')
sleep(2)

driver.find_element_by_name('commit').click()
print('点击提交评论')
sleep(3)

driver.quit() #关闭窗口
