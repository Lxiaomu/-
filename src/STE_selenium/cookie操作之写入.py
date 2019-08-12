# utf-8

# 通过获取cookie信息可知，cookie数据是以字典的形式进行存放的

# 向浏览器中写入cookie

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")
print('开始')
time.sleep(2)

# 向cookie的name 和value中添加会话信息
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})
print('添加')
time.sleep(2)


# 遍历cookies中的name 和value信息并打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

time.sleep(3)
driver.quit()
