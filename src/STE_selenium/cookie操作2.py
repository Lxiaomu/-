# utf-8

# 一般情况下，cookie数据是以字典的形式进行存放的


from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("http://www.youdao.com")
print('进入')
sleep(2)


# 向cookie的name和value中添加会话信息
driver.add_cookie({'name' : 'key-aaaaaaa','value' : 'value-bbbbbb'})
print("name and value")
sleep(2)


# 遍历cookies中的name和value信息并打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'],cookie[')

sleep(3)
driver.quit()
