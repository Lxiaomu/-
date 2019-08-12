# utf-8

# 对于通过input标签实现的上传功能，可以将其看作是一个输入框，
# 即通过send_keys()指定本地文件路径的方式实现文件上传

from selenium import webdriver
import os
from time import sleep


driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get(file_path)
print('准备')
sleep(2)

# 定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')
print('上传')
sleep(2)
driver.quit()
