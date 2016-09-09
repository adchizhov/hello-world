import sys

__author__ = 'Alexander Chizhov'
# checking version
if sys.version_info[0] == 2:
	input_function = raw_input
else:
	input_function = input

que_ans = [('4 * 5 = ', ['20']),
           ("Monty '......'? ", ['Python']),
           ('True or False is ', ['True']),
           ('Nothing in Python ', ['None']),
           ('True and False is ', ['False'])]

CORRECT_ANS = 0
TOTAL_QUE = len(que_ans)
user_name = input_function('Welcome to my quiz! What is your name? ')

for question, answers in que_ans:
    answer = input_function(question)
    if answer in answers:
    	CORRECT_ANS += 1
    	print ('Correct! %s of %s\n' % (CORRECT_ANS, TOTAL_QUE))
    else:
    	print ('NO!\n')
print ('Bye-bye, %s' % (user_name))
