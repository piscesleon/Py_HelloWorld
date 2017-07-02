#! python3
# 搜索一个结果，并打开前几项链接, 未成功

import sys
import requests #另外安装的模块，用于下载网页内容
import bs4
import webbrowser

print('Searching with Baidu...') # display text while downloading the Google page
res = requests.get('http://www.baidu.com/?wd=' + ' '.join(sys.argv[1:]) + '&ie=utf-8')
res.raise_for_status() #trace status

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(soup)
# TODO: Open a browser tab for each result.
linkElems = soup.select('.t a') #r 类仅用于查询结果链接,用选择符'.r a'，找到所有具有 CSS 类 r 的元素中的<a>元素。

numOpen = min(5, len(linkElems)) #有效链接数，与数字5之间，取一个最小值，作为打开页面数量
for i in range(numOpen):
    webbrowser.open('http://www.baidu.com' + linkElems[i].get('href'))
