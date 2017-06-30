#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip # 导入剪贴板
import re # 导入正则表达式

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')

print(lines)

print(len(lines))

for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
print(lines)
print(text)
pyperclip.copy(text)
