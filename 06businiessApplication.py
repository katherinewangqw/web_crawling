# NOTE: https://shimo.im/docs/3tBnAKw2QfQDEsQF/read
# === 爬取实战prepare ===

# --- headers ---

import requests
import re
# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# url = 'http://www.zhihu.com'
# res = requests.get(url, headers = headers).text
# print(res)
# NOTE: 通过非浏览器访问，会显示400 Bad Request；所以要模拟浏览器，使用headers

# --- timeout ---
# res = requests.get(url, headers = headers, timeout = 10).text
# Note: timeout means that if the web has not shown up after 10s, output ERROR instead

# --- 编码的相关知识 ---
# 可能会有乱码的情况，可以在res那一行下面写如下code
# TODO：method 1
# res = res.encode('ISO-8859-1').decode('utf-8')
# TODO：method 2
# res = res.encode('ISO-8859-1').decode('gbk')
# TODO: method cure-all
article = b'\xe7\x8e\x8b\xe9\x92\xa6\xe9\x9b\xaf'
try:
    article = article.decode('utf-8') # method 1
except:
    try:
        article = article.decode('gbk') # method 2
    except:
        article = article # method 0
print(article)

# === 舆情评分 ===
score = []
keywords = ['违约', '诉讼', '兑付', '阿里', '百度', '京东', '互联网']
title = ['京东违约', ' 阿里巴巴诉讼百度']
for i in range(len(title)):
    num = 0
    try:
        article = requests.get(href[i], headers=headers, timeout=10).text
    except:
        article = '爬取失败'

    try:
        article = article.decode('utf-8')  # method 1
    except:
        try:
            article = article.decode('gbk')  # method 2
        except:
            article = article  # method 0

    p_article = '<p>(.*?)</p>' # 有时候正文也会被一并消除，所以这个地方再把它加回去
    article_main = re.findall(p_article, article)
    article = ''.join(article_main)

    for k in keywords:
        if (k in article) or (k in title[i]):
            num -= 5
    score.append(num)
print(score)

# === 搜狐新闻爬取 ===
# NOTE: define a function
def sohu(company):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    url = 'https://news.sogou.com/news?mode=1&sort=0&fixrank=1&query=' + company + '&shid=djt1'
    res = requests.get(url, headers = headers, timeout = 10).text
    # print(res)
    p_href = '<a href="(.*?)" id="uigs.*?" target="_blank">'
    p_title = '<a href=".*?" id="uigs.*?" target="_blank">(.*?)</a>'
    p_date = '<p class="news-from">(.*?)</p>'

    href = re.findall(p_href, res) # 有时候包含re.S也不是什么好事
    title = re.findall(p_title, res, re.S)
    date= re.findall(p_date, res, re.S)

    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        title[i] = re.sub('&.*?;', '', title[i])
        date[i] = re.sub('<.*?>', '', date[i])
        date[i] = re.sub('&.*?;', '', date[i])

    for i in range(len(title)):
        print(str(i+1) + '.' + title[i] + '--' + date[i])
        print(href[i])

# TODO: uncomment below to text
# companies = ['阿里巴巴','网易云','谷歌']
# for i in companies:
#     try:
#         print('---start for company' + i + '---')
#         sohu(i)
#         print('---done for company' + i+ '---' + '\n')
#     except:
#         print(i + 'has Error!')

# === 中国经营报官网 ===

def jy(company):
    url = 'http://zhannei.baidu.com/cse/search?s=1769878842797832208&entry=1&q=' + company
    res = requests.get(url).text # NOTE: 这里需要编译
    res = res.encode('ISO-8859-1').decode('utf-8')
    # print(res)
    p_href = '<a rpos="" cpos="title" href="(.*?)"  target="_blank">.*?</a>'
    p_title = '<a rpos="" cpos="title" href=".*?"  target="_blank">(.*?)</a>'
    p_date = '<span class="c-showurl" >(.*?)</span>'

    href = re.findall(p_href, res)
    title = re.findall(p_title, res)
    date = re.findall(p_date, res)

    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        date[i] = date[i].split(' ')[1]  # NOTE: 通过split来分隔开我们需要的信息

    print(href)
    print(title)
    print(date)

#jy('阿里巴巴') # TODO: Test

# === 数据清理 ===

data = ['\r\n2019.01.02 15:45:40\n','\r\n2018.04.01 15:45:40\n','\r\n2020.05.20 15:45:40\n']
for i in range(len(data)):
    data[i] = data[i].strip()
    data[i] = data[i].split(' ')[0]
    data[i] = re.sub('[.]', '-', data[i])  # Note: using [] to notify that . is not a regular expression here
    print(data[i])













