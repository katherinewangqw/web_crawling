
#
# import pdfplumber
# import os
#
# # 1.遍历文件夹中的所有PDF文件
# file_dir = r'E:\演示文件夹'  # 改成你自己需要遍历的文件夹
# file_list = []
# for files in os.walk(file_dir):  # 遍历该文件夹及其里面的所有子文件夹
#     for file in files[2]:
#         if os.path.splitext(file)[1] == '.pdf' or os.path.splitext(file)[1] == '.PDF':
#             file_list.append(file_dir + '\\' + file)
# print(file_list)
#
# # 2.PDF文本解析
# for i in range(len(file_list)):
#  pdf = pdfplumber.open(file_list[i])
#  pages = pdf.pages
#  text_all = []
#  for page in pages: # 遍历pages中每一页的信息
#  text = page.extract_text() # 提取当页的文本内容
#  text_all.append(text) # 通过列表.append()方法汇总每一页内容
#  text_all = ''.join(text_all) # 把列表转换成字符串
#  print(text_all) # 打印全部文本内容
#  pdf.close()