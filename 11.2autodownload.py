# === 模拟翻页 ===
from selenium import webdriver
import time
import re
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=理财'
browser.get(url)
time.sleep(3) # 给时间让浏览器反应一下
data = browser.page_source
# --- 应该翻几页？ --- NOTE：通过合计多少条来确定
p_count = '<span class="total-box" style="">约 (.*?) 条 当前显示1-10条</span>'
count = re.findall(p_count, data)[0]
pages = int(int(count)/10) # 这里需要将有可能的小数换成整数
#browser.find_element_by_xpath('//*[@id="pagination_title"]/ul/li[12]').click()
#browser.find_element_by_xpath('//*[@id="fulltext-search"]/div/div[1]/div[2]/div[4]/div[2]/div/button[2]').click()
browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[4]/div[2]/div/button[2]').click()
datas = []
datas.append(data) # 这边是把刚刚获取的第一页源代码先放到datas这个列表里
for i in range(2): # 刚刚获取到的pages页码数
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[4]/div[2]/div/button[2]').click()
    time.sleep(2)
    data = browser.page_source
    datas.append(data)
    time.sleep(1)
alldata = "".join(datas) #把列表转换成字符串
browser.quit()
#print(alldata)

p_title = '<span title="" class="r-title">(.*?)</span>'
p_href = '<td rowspan="1" colspan="1" class="el-table_1_column_2  "><div class="cell"><a target="_blank" href="(.*?)" data-id='
p_date = 'class="el-table_1_column_3 is-left "><div class="cell"><span class="time">(.*?)</span>'
title = re.findall(p_title, alldata)
href = re.findall(p_href, alldata)
date = re.findall(p_date, alldata, re.S)

for i in range(len(title)):
    title[i] = re.sub('<.*?>', '', title[i])
    date[i] = date[i].strip()
    p_id = 'announcementId=(.*?)&amp'
    id = re.findall(p_id, href[i])
    id = ''.join(id)
    href[i] = 'http://static.cninfo.com.cn/finalpage/' + str(date[i]) + '/' + str(id) + '.PDF'
    for k in range(1):
        chrome_options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': '/Users/katherinewang/Desktop/dltest'}
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get(href[i])
        try:
            browser.find_element_by_xpath('/html/body/viewer-pdf-toolbar//div[1]/div[1]/div[2]/cr-icon-button[2]').click()
            time.sleep(3)
            print('success')
            browser.quit()
        except:
            print('Error occurs when downloading')
    print(str(i + 1) + '.' + title[i] + ' - ' + date[i])
    print(href[i])

