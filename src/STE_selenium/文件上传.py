#  utf-8

# 该文件需配合上传功能使用

# 以下仅是例子

from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('upfile.html')
print('上传功能地址')
time.sleep(2)
driver.get(file_path)
print('打开上传功能网页')
time.sleep(5)

# 定位上传按钮，添加本地文件
file_a = driver.find_element_by_name('file')
print('定位上传按钮')
time.sleep(2)
file_a.send_keys('D:\\upload_file.txt')
print('添加文件')
time.sleep(2)


driver.quit()
