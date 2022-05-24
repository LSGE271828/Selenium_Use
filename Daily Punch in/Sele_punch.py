from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
browser = webdriver.Chrome(options=options)


browser.find_element_by_id('user_name').send_keys("XXX")
browser.find_element_by_name('password').send_keys("XXX")
# 替换为自己的昵称,密码
browser.find_element_by_id('login').click()
time.sleep(2)


time.sleep(1)
print(browser.title)
kw =browser.find_elements(By.XPATH,"//*[@class='block-group__item__wrap']")[8].click()
time.sleep(3)

#窗口句柄操作
win1 = browser.window_handles
browser.switch_to.window(win1[1])
browser.implicitly_wait(3)
browser.find_element(By.ID,'login-submit').click()


browser.find_elements(By.XPATH,"//div[@class='center']")[14].click()
browser.implicitly_wait(30)
browser.find_elements(by=By.TAG_NAME,value="button")[0].click()
browser.implicitly_wait(30)

browser.find_elements(By.XPATH,"//div[@class='commandC']/ul/li")[0].click()
browser.implicitly_wait(30)
browser.find_elements(By.XPATH,"//div[@class='dialog_footer']/button")[0].click()
browser.implicitly_wait(30)
browser.find_elements(By.XPATH,"//div[@class='dialog_footer']/button")[0].click()

