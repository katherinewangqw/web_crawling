# === advanced application of text processing ===

# --- define a function ---

# it is important to import the following functions
import requests
import re

def baidu(company):
    key = company
    url = 'http://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=' + key
    print(url)
    #res = requests.get(url).text

# 单个搜索
baidu('618')

# 多个搜索，使用list
companys = ['王者荣耀', '阴阳师', '炉石传说', 'fgo']
for i in companys:
    baidu(i)

print('---locate info---')

# define the info u want using regular expression
p_href = '<h3 class="c-title">.*?"(.*?)"'
# call 'findall' to output those information
'''remember! this href outputs as a list!'''
href = re.findall(p_href, res, re.S)


print('---file writer---')

# create a txt file to record
# file1 = open('地址', 'a')
# file1.write('要写的东西')
# for j in range(len(title)):
#     file1.write(title啊日期之类的信息)
# file1.write('---------------------------------------------' + '\n' + '\n')

print('---try except---')

# in order to prevent unwanted error to stop all codes
# try:
#     codes
# except:
#     print('code')

