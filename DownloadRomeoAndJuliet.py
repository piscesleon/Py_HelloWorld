#! python3
# 这里放程序说明

import os
import requests #另外安装的模块，用于下载网页内容
import logging #导入日志

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# TODO: 这里放置所有待办事项

# 以下放置代码
os.chdir('D:\\Project\\Python')
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000): #每10万字节写入一次
    playFile.write(chunk)
playFile.close()
