# utf-8
"""
 例子：
 <html>
   <body>
     ...
     <iframe id = "x-URS-iframe" ...>
       <html>
           <body>
              ...
               <input name = "email">
  上面代码：126邮箱登录框的结构便是表单嵌套的。想操作登录框必须要先切换到iframe表单中
"""
# switch_to.frame() 默认可以直接取表单的id 或name属性
# switch_to.default_content()   跳回最外层的页面

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.126.com")
print("进入")
sleep(2)
driver.refresh() #刷新页面
sleep(3)
driver.maximize_window()  #浏览器最大化
sleep(3)



driver.find_element_by_id('lbNormal').click()

# contains(a,b)        如果a中含有字符串b，在返回true,否则返回false
# starts-with(a,b)     如果a是以字符串b开头，返回true,否则返回false
# ends-with(a,b)       如果a是以字符串b结尾，返回true,否则返回false

xf = driver.find_element_by_xpath("//iframe[starts-with(@id , 'x-URS-iframe')]")
print('定位到iframe中')
sleep(2)
driver.switch_to.frame(xf)
print('跳转到iframe界面')
sleep(2)


"""
# 页面表单跳转时重新聚焦
driver.switch_to.window(driver.window_handles[0])
print('聚焦')
sleep(2)

"""
driver.find_element_by_name("email").clear()
print("定位到账号输入框并清除文本框")
sleep(2)
# 定位到账号框并输入值
driver.find_element_by_name('email').send_keys("lrm1106361798")
print("定位到账号输入框并输入")
sleep(2)

driver.find_element_by_name('password').clear()
print("定位到密码输入框并清除密码框文本")
sleep(2)
# 定位到密码框并输入值
driver.find_element_by_name('password').send_keys("lrm149206lrm")
print("定位到密码输入框并输入")
sleep(2)

# 定位到登录按钮并点击
driver.find_element_by_id('dologin').click()
print("点击登录")
sleep(2)

# 返回最外层
driver.switch_to.default_content()  
print("gg")
sleep(2)


driver.quit()
