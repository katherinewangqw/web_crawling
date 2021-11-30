# === multiple at a time ===

import requests
import re

# NOTE: how to get page 2 page 3?
# change page number

def baidu(company, page):
    num = page * 10
    url = 'http://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=' + company + '&pn=' + str(num)
    res = requests.get(url).text

    print('---page ' + str(page + 1) + '---')

    p_href = '<h3 class="c-title">.*?"(.*?)"'
    p_title = '<h3 class="c-title">.*?>(.*?)</a>'
    title = re.findall(p_title, res, re.S)
    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i]).strip()
        href = re.findall(p_href, res, re.S)
        print(str(i + 1) + '.' + title[i])
        print(href[i])

companys = ['Dior', 'YSL']
# TODO: uncomment below if you want to test:
# try:
#     for a in range(len(companys)):
#         for b in range(2):  # how many pages you want
#             baidu(companys[a], b)
#         print('---complete for ' + companys[a] + '---' + '\n')
# except:
#     print('error occurs!!!!')

# === 按照时间排序 ===

# NOTE: change the url's content, from rrt=1 to rrt=4

# === 爬取总新闻数 ===

# here's a copy paste code direct form Baidu
example = '''</div>
</div>
<div id="header_top_bar">
	<span class="nums">找到相关资讯约1,440,000篇</span>'''

p_news_num = '<span class="nums">(.*?)</span>'
# NOTE: remember, news_num is a list!
news_num = re.findall(p_news_num, example)
# TODO: uncomment below if want to see the result
# print(news_num[0])

# === 正文爬取及舆情评分系统搭建 ===

score = []
keywords = ['违约', '诉讼', '税负', '阿里', '百度', '腾讯', 'Dior']
# the following href and title is an example
title = ['百度违约', '阿里对腾讯提起诉讼']
href = 'http://sports.sina.com.cn/chaoliu/2020-06-22/doc-iirczymk8298028.shtml'
for i in range(len(title)):
    num = 0
    # NOTE: visit href will get the main content
    # 有时候可能会在爬取正文的时候 出现异常，那么可以在这里添加try except
    article = requests.get(href).text
    for k in keywords:
        if (k in article) or (k in title[i]):
            num -= 5  # 如果有关键词，就扣5分
    score.append(num)
print(score)
