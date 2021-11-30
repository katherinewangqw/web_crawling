# === 文字识别 ===
from aip import AipOcr

# 下面3行内容为自己的APP_ID,API_KEY,SECRET_KEY
APP_ID = '21215216'
API_KEY = 'pFGKdDbVvG5Zt5lYHSeWcAg4'
SECRET_KEY = 'xg32ehtqpdPglSP0w26ZZLlAkDD8KkWP'
# 把上面输入的账号信息传入接口
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 自己图片的地址，其他地方就不用改了
filePath = r'诗.jpg'
# 定义打开文件的函数
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
# 定义参数变量
options = {
'detect_direction': 'true',
'language_type': 'CHN_ENG',
}
# 调用通用文字识别接口并打印结果
result = aipOcr.basicGeneral(get_file_content(filePath), options)
print(result)
# 打印具体内容
words_result = result['words_result']
for i in range(len(words_result)):
    print(words_result[i]['words'])

# === 人脸识别 ===
from aip import AipFace
import base64
# 下面3行内容为自己的APP_ID,API_KEY,SECRET_KEY
APP_ID = '16994639'
API_KEY = 'L9XnkKQEMnHhB5omF2P8D9OM'
SECRET_KEY = 'nnOZDoruZ6AjVglBs6ecvUjFRIAKrn9T'
# 把上面输入的账号信息传入接口
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)
# 下面一行内容为需要识别的人脸图片的地址，其他地方就不用改了
filePath = r'IMG_5972.jpeg'
# 定义打开文件的函数
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        content = base64.b64encode(fp.read())
        return content.decode('utf-8')
imageType = "BASE64"
# 选择最后要展示的内容，这里展示age;gender;beauty
options = {}
options["face_field"] = "age,gender,beauty"
# 调用接口aipFace的detect()函数进行人脸识别，打印结果
result = aipFace.detect(get_file_content(filePath), imageType, options)
print(result)