#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip # 导入剪贴板
import re # 导入正则表达式


# 以下放置测试代码

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242., 111-222-3322')
print('Phone number found: ' + mo.group())
