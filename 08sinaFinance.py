# === 新浪财经爬取 ===
import requests
import re
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# NOTE: %%中的内容不能用英文替换，这也是这个网站爬取的难点
def sino(company,code):
    url = 'https://search.sina.com.cn/?q=' + code + '&range=all&c=news&sort=time'
    res = requests.get(url, headers=headers, timeout=10).text

    p_href = '<h2><a href="(.*?)" target="_blank">.*?</a>'
    p_title = '<h2><a href=".*?" target="_blank">(.*?)</a>'
    p_date = '<span class="fgray_time">(.*?)</span></h2>'

    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)
    date = re.findall(p_date, res, re.S)

    for i in range(len(title)):
        date[i] = date[i].strip()
        date[i] = date[i].split(' ')[1]
        title[i] = re.sub('<.*?>', '', title[i])
        print(str(i + 1) + '.' + title[i] + ' - ' + date[i])
        print(href[i])

# NOTE: method 1 -- copy and paste the coded chinese character on the website
# sino('%B0%A2%C0%EF%B0%CD%B0%CD')

# NOTE: method 2 -- use dictionary
# 每一个公司在新浪财经对应的英文编码是不变的，那么我们就可以通过字典的方式，把公司名称和其在新浪财经上对应的英文格式放到一起。

# TODO: let us review a bit about dictionary
# test = {'Ana': '1', 'Bob':'2'}
# print(test['Ana'])
# for i in test:
#     print(i)
#     print(test[i])

companys = {'阿里巴巴':'%B0%A2%C0%EF%B0%CD%B0%CD','万科集团':'%CD%F2%BF%C6%BC%AF%CD%C5','华能信托':'%BB%AA%C4%DC%D0%C5%CD%D0'}
for i in companys:
    print('--- start for ' + i + '---')
    # sino(i, companys[i]) #TODO: uncomment to test
    print('\n')

# NOTE: method 3 -- encode Chinese characters
from urllib.parse import quote
companys1 = ['阿里巴巴', '万科集团', '华能信托']
companys2 = {}
for i in companys1:
    code = quote(i.encode('gbk'))
    companys2[i] = code
for i in companys2:
    xinlang(i, companys2[i])