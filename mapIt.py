#! python3
# 这里放程序说明

import webbrowser
import sys
import re # 导入正则表达式


if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:]) # 返回的列表中，第1个值为py程序名，因此以 [1:] 规避第1个参数
# print(sys.argv) # 测试返回的列表
print(address)

webbrowser.open_new_tab('https://www.baidu.com/s?wd='+address)

