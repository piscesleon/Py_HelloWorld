#! python3
# 从剪贴板中取得所有电话与email地址

import pyperclip # 导入剪贴板
import re # 导入正则表达式


# 以下放置测试代码

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # 1area code 仅1对括号，因右边的\(和\)是转义符
    (\s|-|\.)? # 2separator
    (\d{3}) # 3first 3 digits
    (\s|-|\.) # 4separator
    (\d{4}) # 5last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # 6-8对括号，顺序应该是按左括号出现的顺序来计算 extension
    )''', re.VERBOSE)

# Create email regex.

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @ # @ symbol
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4}) # dot-something 问题，这里只识别了带一个.号，且后缀为2-4位的地址
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text): # phoneRegex是之前已经定义过的模式，即在text中用之前定义的模式查找结果
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0]) # 0,或不传入参数，表示整个匹配的文本


# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


'''
测试数据如下

asdf (415)-863-9900
415-863-9950 ext 234 adsfad
234 info@nostarch.com
media@nostarch.com cc
dd academic@nostarch.com
help@nostarch.com aa
'''
