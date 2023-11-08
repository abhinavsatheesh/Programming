print ('Hello. Welcome to The Operations Program of Python.')
question=int (input('Enter a number'))
question1=int (input('Enter another number'))
operatorquestion=input('What is the operation you wish to do? Type the symbol.')
if operatorquestion=='+':
    print (question+question1)
if operatorquestion=='-':
    print (question-question1)
if operatorquestion=='*':
    print (question*question1)
if operatorquestion=='/':
    print (question/question1)