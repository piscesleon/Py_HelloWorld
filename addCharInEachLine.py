#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste() # 以剪贴板中的数据赋值给text

# Separate lines and add stars.

lines = text.split('\n') # 把text按换行符分离为列表，并保存到lines

print(lines) # 查看分离后的结果

# print(len(lines))

for i in range(len(lines)): # 遍历lines列表中的每个元素
    lines[i] = '* ' + lines[i] # 在lines列表中的每个元素前加上 '* '
text = '\n'.join(lines) # 用join把lines中的列表项组合为一个字符串
print(text) # 查看完成合并的字符串
pyperclip.copy(text) # 复制字符串到剪贴板
