#! python3
# 遍历d:\Project下的所有文件夹与文件

import os
import re # 导入正则表达式
import pyperclip # 导入剪贴板
import shelve # 导入用于保存变更的二进制文件模块


# 以下放置代码


for folderName, subfolders, filenames in os.walk('D:\\Project'): # 遍历所有文件夹、及子文件夹，并用for列出所有父子文件夹与文件名
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print('')
