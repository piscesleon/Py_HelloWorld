#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta',
            'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing',
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.

for quizNum in range(35):

    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w') # 建立或打开1-35文件，设置为写模式
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w') # 建立或打开1-35答案文件，设置为写模式

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys()) #获取capital键列表
    random.shuffle(states) #随机排序

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]] #获取正确答案
        wrongAnswers = list(capitals.values()) #创建错误答案第1步，获取所有答案值
        del wrongAnswers[wrongAnswers.index(correctAnswer)] #创建错误答案第2步，删除正确答案
        wrongAnswers = random.sample(wrongAnswers, 3) #创建错误答案第3步，随机取样3个剩余答案
        answerOptions = wrongAnswers + [correctAnswer] #把正确答案和错误答案拼接起来
        random.shuffle(answerOptions) #随机打乱顺序

    # Write the question and answer options to the quiz file.
    quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
    for i in range(4):
        quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i])) # 双参数写入
    quizFile.write('\n')
    # Write the answer key to a file.
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()

