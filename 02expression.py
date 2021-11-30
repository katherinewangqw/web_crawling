'''title & author'''

# import requests
# key = '华为'
# url = 'http://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=' + key
# res = requests.get(url).text
# print(res)

# ===regular expression===

# --- findall ---
import re
# content = 'Hello 123 world 456 this is just 789 a test'
# result = re.findall('\d\d\d', content)  # want to find 3 digits
# print(result)  # the result is an array
# a1 = result[0]
# print(a1)

print('example')
# res = '<p class="c-author">新浪新闻&nbsp;&nbsp;5小时前</p>'
# res2 = '<em>阿里巴巴</em>"（中国）网络技术有限公司12年"<em>阿里巴巴</em>"公司赔偿30万人民币'
# p_source = '<p class="c-author">(.*?)&nbsp'
# p_date = '&nbsp;&nbsp;(.*?)</p>'
# p_text = '</em>(\w*)'
# source = re.findall(p_source, res)
# print(source)
# date = re.findall(p_date, res)
# print(date)
# text = re.findall(p_text, res2)
# print(text)

# ---how to ignore linefeeds---
# use the '''''' to enter the code you want to include \n
# res = '''<div class="result" id="3">
# <h3 class="c-title">
#  <a href="http://baijiahao.baidu.com"
#     data-click="{
#       'f0':'77A717EA',
#       'f1':'9F63F1E4',
#       'f2':'4CA6DE6E',
#       'f3':'54E5243F',
#       't':'1592443086'
#       }"
#                 target="_blank"
#             >
#       入职<em>阿里巴巴</em>12年被指“不能胜任工作”,被裁员工获赔
#     </a>
# </h3>'''
# p_href = '<h3 class="c-title">.*?<a href="(.*?)"'
# p_title = '<h3 class="c-title">.*?>(.*?)</a>'
# href = re.findall(p_href, res, re.S)  # use re.S to ignore linefeeds
# title = re.findall(p_title, res, re.S)
# print(href)
# print(title)

# ---how to get rid of <em> and </em>---
# have to be in the form of an array
# title = ['入职<em>阿里巴巴</em>12年被指“不能胜任工作”,被裁员工获赔']

# method 1 - replace
# title[0] = title[0].replace('<em>','')
# title[0] = title[0].replace('</em>','')
# print(title)

# method 1 - substitute
# '''⬇️替换完成后的标题         ⬇️替换后的内容：空'''
# title[0] = re.sub('<.*?>', '', title[0])
# '''       需要替换的内容⬆️           ⬆️原来的标题'''
# print(title)

# ---how to replace * ---
#
# test = 'like the *way you lie'
# test = re.sub('[*]', '', test)
# # use brackets[] to make it lose the special meaning it has
# print(test)
