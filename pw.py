#! python3
# pw.py - An insecure password locker program.

# Password Dictionary
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys

if len(sys.argv) < 2: # 判断sys.argv的参数是否小于2个  sys.argv是用于命令行方式执行程序的参数
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name 即第一个参数为需要取出PW的账户名

if account in PASSWORDS:
    # pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' is ' + PASSWORDS[account])
else:
    print('There is no account named ' + account)

# 可以用以下命令行方式来执行本程序
# python pw.py email
