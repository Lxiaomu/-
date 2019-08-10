# utf-8

# switch_to.window()方法，可以实现在不同的窗口之间切换.
# 与上一节的switch_to.frame()类似，前者用于不同窗口的切换，后者用于不同表单之间的切换。
# current_window_handle：获得当前窗口句柄
# window_handles：返回所有窗口的句柄到当前会话
#

# 以百度首页和百度注册页为例，在两个窗口之间的切换
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle
print('11')
time.sleep(2)

# 定位到登录按钮并点击
driver.find_element_by_link_text('登录').click()
print('22')
time.sleep(2)

# 定位到立即注册按钮并点击
driver.find_element_by_link_text("立即注册").click()
print('3')
time.sleep(2)

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles
print('11')
time.sleep(2)


# 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        time.sleep(2)
        driver.find_element_by_name("account").send_keys('username')
        print('登录')
        time.sleep(2)
        driver.find_element_by_name('password').send_keys('password')
        print('密码')
        time.sleep(2)
        # ……


driver.quit()
