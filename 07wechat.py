# === IP代理 ===
# 为了防止在短时间访问同一个网站太多次之后，被拉入黑名单
# 把自己的IP伪装成从IP代理池里提取到的IP，从而躲过某些网站对于固定IP访问次数的限制
# NOTE: http://www.xdaili.cn/yzapi (购买link）
import requests
import re
import time
# proxy = '218.74.81.58:40335'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# proxy = requests.get('http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=2846a61f23074da098db9a60f3d41eb8&orderno=YZ2020736173x0DFau&returnType=1&count=1').text
# proxy = proxy.strip()  # NOTE: this is important because we gotta get rid of \n
# proxies = {"http":"http://"+proxy,"https":"https://"+proxy}
# url = 'https://ip.cn/'
# res = requests.get(url, proxies = proxies, headers = headers, timeout = 10).text
# print(res)

# === Wechat Crawl ===
def weixin(company):
    url = 'https://weixin.sogou.com/weixin?type=2&query=' + company
    res = requests.get(url, headers = headers, timeout = 10, proxies = proxy).text
    # --- add proxy ---
    proxy = requests.get('http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=2846a61f23074da098db9a60f3d41eb8&orderno=YZ2020736173x0DFau&returnType=1&count=1').text
    proxy = proxy.strip()  # NOTE: this is important because we gotta get rid of \n
    proxies = {"http":"http://"+proxy,"https":"https://"+proxy}
    # TODO: href 反爬
    p_href = '<a target="_blank" href="(.*?)" id="sogou'
    p_title = 'article_title_.*?">(.*?)</a>'
    p_date = 'timeConvert\(\'(.*?)\'\)'   # NOTE: need to be converted to normal form

    href = re.findall(p_href,res)
    title = re.findall(p_title, res)
    date = re.findall(p_date,res)

    for i in range(len(title)):
        title[i] = re.sub('<.*?>','', title[i])
        title[i] = re.sub('&.*?;', '', title[i])
        href[i] = re.sub('amp:','',href[i])

        # --- how to convert time form ---
        timestamp = int(date[i])
        timeArray = time.localtime(timestamp)
        date[i] = time.strftime("%Y-%m-%d", timeArray)

        print(str(i+1) + '.' + title[i] + ' -- ' + date[i])
        # print(href[i])  # NOTE: still have problem

weixin('阿里巴巴')