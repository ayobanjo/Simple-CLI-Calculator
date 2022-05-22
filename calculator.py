
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
% for modulus
''')



firstNumber = int(input('Enter your first number: '))
secondNumber = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(firstNumber, secondNumber))   #prints out the format method to show the values inputed
    print(firstNumber + secondNumber) 

elif operation == '-':
    print('{} - {} = '.format(firstNumber, secondNumber))
    print(firstNumber - secondNumber)

elif operation == '*':
    print('{} * {} = '.format(firstNumber, secondNumber))
    print(firstNumber * secondNumber)

elif operation == '/':
    print('{} / {} = '.format(firstNumber, secondNumber))
    print(firstNumber / secondNumber)
elif operation == '%':
    print('{} % {}= ' .format(firstNumber, secondNumber))
    print(firstNumber % secondNumber)

else:
    print('Choose valid operator, then run again.')