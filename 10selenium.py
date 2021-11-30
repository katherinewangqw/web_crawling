# === selenium and chrome driver===

# 找不到财经指数，怎么办呢？
# 添加Chrome driver
# import requests
# url = 'http://finance.sina.com.cn/realstock/company/sh000001/nc.shtml'
# res = requests.get(url).text

# === 如何模拟百度搜索？===
# 模拟人工操作浏览器
from selenium import webdriver
# --- 无界面浏览器设置 ---
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()  # 页面最大化
link = "http://finance.sina.com.cn/realstock/company/sh000001/nc.shtml"
browser.get(link)

# === 模拟键入和搜索 ===
# --- method 1. xpath ---
# browser.find_element_by_xpath('xpath内容')  # copy Xpath
# browser.find_element_by_xpath('//*[@id="kw"]').send_keys('python') # NOTE: send keys to python模拟了键盘输入
# browser.find_element_by_xpath('//*[@id="su"]').click()

# --- method 2. css_selector ---
# browser.find_element_by_css_selector('#kw').send_keys('python')
# browser.find_element_by_css_selector('#su').click()

data = browser.page_source  # get page source
print(data)
browser.quit()  # 关闭模拟浏览器
