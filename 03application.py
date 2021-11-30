# ===text processing (title, date & source)===

print('review')  # review for basic steps

# 百度新闻搜索词条
# f12+查看网页原代码
# use code to get 源代码

# 这里放一则新闻的整个源代码
# 可以从中发现一些规律
res1 = '''<div class="result" id="6">
<h3 class="c-title">
 <a href="https://baijiahao.baidu.com/s?id=1669732476189848475&amp;wfr=spider&amp;for=pc"
    data-click="{
      'f0':'77A717EA',
      'f1':'9F63F1E4',
      'f2':'4CA6DE6E',
      'f3':'54E5243F',
      't':'1592446630'
      }"
                target="_blank"
            >
      入职<em>阿里巴巴</em>12年被指“不能胜任工作”,被裁员工获赔
    </a>
</h3>
<div class="c-summary c-row ">
      <p class="c-author">
              <img class="source-icon" src="https://cambrian-images.cdn.bcebos.com/90a3cc56048cc77b55e93b3d1ba00c0b_1642383032504386.jpeg@w_100,h_100" alt="" />
        新浪财经&nbsp;&nbsp;            				
						2020年06月17日 11:49
			
    </p>
    (2018年1月1日至2018年3月31日)绩效成绩也为3.25B,属于“不胜任工作&quot;,<em>阿里巴巴</em>公司于2018年8月29日向集团工会征求意见,工会亦对解除决定不持异议,决定何某某...
    <span class="c-info">
                    <a href="http://cache.baidu.com/c?m=9d78d513d9d431ad4f9e94697c14c0116d43f0612ba6a6020fd68439e5701c011969b9fd61605113d2b6617a51fc1204b1a36c216a1420c0cb9bd31c9aac925f7ed57829310b873549850eaebd4521c52b955be9a91ce3b9fa3999a8d8d5da5344ca57402ec0e78a2c41569139a75426e3a2cd15554811ccaf61&amp;p=87769a47ca8307b40fbd9b7d53&amp;newp=c9769a47cddd1cff57eecd221553d8265f15ed6028818b783b83d309c839074e4765e7b121251707d7ce68216cee1e1ee5a76a242c1d7d&user=baidu&fm=sc&query=%B0%A2%C0%EF%B0%CD%B0%CD&qid=98c563ca00540e00&p1=6"
      data-click="{'fm':'as_l'}"
        target="_blank"  class="c-cache">
                百度快照</a>
              </span>
      </div>
</div>
'''

es2 = '''</div>
</div>
<div id="header_top_bar">
	<span class="nums">找到相关资讯约1,440,000篇</span>'''

# ---get page source & the info we want---

# import requests and regular expression
import requests
import re
import time

# get the page source
# define a function to get multiple info in one time
def baidu(company):
    key = company
    url = 'http://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=' + key
    print('现在正在爬取' + company)
    print(url)
    res = requests.get(url).text

    # use regular expression
    p_href = '<h3 class="c-title">.*?"(.*?)"'
    p_title = '<h3 class="c-title">.*?>(.*?)</a>'

    # 因为这里有些source有image的链接，需要把它去除的话需要一个indicator
    # 这里愚蠢的选择了少打一个&，为了后续定位image link的位置
    # 可能有其他更好的方法，但我只会到这里
    p_source = '<p class="c-author">(.*?)nbsp;&nbsp;'
    p_date = '<p class="c-author">.*?&nbsp;&nbsp;(.*?)</p>'
    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)
    source = re.findall(p_source, res, re.S)
    date = re.findall(p_date, res, re.S)

    # use function strip to get rid of spaces and \n\t
    for i in range(len(date)):
        date[i] = date[i].strip()
        href[i] = href[i].strip()
        # 去除title中的<em>和</em>
        title[i] = re.sub('<.*?>', '', title[i]).strip()
        # 因为有的title有link，有的没有，所以选择写了一个if loop
        if '<img' in source[i]:
            p_clear = '<img class=.*?/>(.*?)&'
            source[i] = re.findall(p_clear, source[i], re.S)
            # 因为这里list中的每个element都是个list，所以要把每个element转变为str，
            # 所以使用了join命令，不然不能使用strip指令
            source[i] = ''.join(source[i]).strip()
        else:
            p_ignore = '(.*?)&'
            source[i] = re.findall(p_ignore, source[i], re.S)
            source[i] = ''.join(source[i]).strip()
    # create a txt file to record
    # 每次run会在txt文件后面加新的内容
    file1 = open('/Users/katherinewang/Desktop/test.txt', 'a')
    file1.write(company + '舆情监控completed!' + '\n' + '\n')
    for j in range(len(title)):
        # 和print一样，但是这里用了filewrite
        # txt不会自动换行，所以用了\n
        file1.write(str(j + 1) + '.' + title[j] + '(' + date[j] + '-' + source[j] + ')' + '\n')
        file1.write(href[j] + '\n')
    file1.write('---------------------------------------------' + '\n' + '\n')

while True:
    companies = ['博世', '贾菊韵']
    for i in range(len(companies)):
        try:
            baidu(companies[i])
            print(companies[i] + '爬取成功' + '\n')
        except:
            print('!!!!!error occurred at ' + companies[i])
    time.sleep(5)  # run every 10800s = 3 hours
