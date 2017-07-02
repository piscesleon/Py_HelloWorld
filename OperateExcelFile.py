#! python3
# 操作Excel文件
# 用到openpyxl模块，官方文档位于 https://openpyxl.readthedocs.io/en/default/

import os
import re # 导入正则表达式
import pyperclip # 导入剪贴板
import shelve # 导入用于保存变更的二进制文件模块
import openpyxl #用于处理Excel文件

import logging #导入日志

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Coding start

os.chdir('D:\\Project\\Python\\Py_HelloWorld')
wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))
print(wb.get_sheet_names()) #打印原文件中的Sheet列表，按原有顺序

#变更Sheet列表中的顺序
SheetList=wb.get_sheet_names()
SheetList.sort(key=str.lower)
print(SheetList)

# 把SheetList中的第一个Sheet，赋值给Sheet1
Sheet1=wb.get_sheet_by_name(SheetList[0])
print(Sheet1)

print(Sheet1.title) #输出对应的Sheet名

# activeSheet=wb.get_active_sheet() #获取当前激活的Sheet
activeSheet=wb.active
print(activeSheet.title) #输出对应的Sheet名

print(Sheet1['A1'].value) #取Sheet1的A1单元格内容
print(activeSheet['A1'].value) #取ActiveSheet的A1单元格内容
print(activeSheet['A2'].value) #取ActiveSheet的A2单元格内容,如果是公式，输出的是公式的具体内容而不是结果

#输出对应的单元格名称
c1=activeSheet['A2'] #将ActiveSheet的A2单元格指定给c1
print(c1.coordinate) #输出c1对应的单元格名称
print('Column of c1 is ' + str(c1.column) + ', Row of c1 is ' + str(c1.row)) #分别输出c1对应的列名(A,B,C....)与行号

# 也可以用数字指定列号
for i in range(1,7,2): #可接受3个参数，起始值、结束值、步长
    print(i, activeSheet.cell(row=i, column=2).value) # 输出active sheet中第2列（B列）1到8行的内容
