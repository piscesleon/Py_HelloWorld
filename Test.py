#! python3
# 这里放程序说明

import pyperclip # 导入剪贴板
import re # 导入正则表达式

# TODO: 这里放置所有待办事项

# 以下放置代码

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242., 111-222-3322')
print('Phone number found: ' + mo.group())
