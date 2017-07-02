#! python3
# 这里放程序说明

import os
import re # 导入正则表达式
import pyperclip # 导入剪贴板
import shelve # 导入用于保存变更的二进制文件模块
import requests #另外安装的模块，用于下载网页内容
import bs4

import logging #导入日志

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# TODO: 这里放置所有待办事项

# 以下放置代码

'''
res = requests.get('http://www.sohu.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)
print(noStarchSoup)
'''

os.chdir('D:\\Project\\Python\\Py_HelloWorld')
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(),"html.parser")
elems = exampleSoup.select('#author') #寻找id author
print(type(elems)) # 获取elems类型，为 list
print(len(elems)) # 长度为1
print(type(elems[0])) # 第1个列表项为bs4.element.Tag类
print(elems[0].getText()) #获取第1个列表项内的文本内容，即id author对应的文本内容
print(str(elems[0])) #获取第1个列表项，含HTML语法的内容
print(elems[0].attrs) #把Tag的所有HTML属性作为一个字典
