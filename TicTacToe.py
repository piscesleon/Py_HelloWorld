# 井字游戏

# 定义空白棋盘
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# 定义 printBoard() 函数，为打印棋盘
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# 设置默认的落子为 X
turn = 'X'


for i in range(9): # 设置落子共9子
    printBoard(theBoard) #先输出目前的棋盘情况
    print('Turn for ' + turn + '. Move on which space?') #输出目前为X/O的步骤，并要求输入落在哪个位置
    move = input() #输入位置
    theBoard[move] = turn #设置字典theBoard的move位置的落子为turn的值
    if turn == 'X': #若turn为X，则变更下一个落子为O
        turn='O'
    else: #否则设置下一外落子为X
        turn='X'

printBoard(theBoard) #9步后输出最终结果
