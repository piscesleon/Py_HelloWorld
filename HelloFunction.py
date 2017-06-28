def HelloF():
    print('Hello1')
    print('Hello2')

HelloF()

def hello(name):
    print('Hello ' + name)

hello('Leon')

import random
def getAnswer(answerNumber):
    if answerNumber==1:
        return 'OK 1'
    elif answerNumber==2:
        return 'OK 2'
    else:
        return 'Other number'

r=random.randint(1,5)
print(r)
print(getAnswer(r))

