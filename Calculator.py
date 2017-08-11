''' Calculator v0.3 '''

'''

Addition: +
Subtraction: -
Multiply: *
Division: /
Sq: **
SqRt: ** 1.0/

'''

import time

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mult(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

def sq(num1,num2):
    return num1 ** num2

def sqrt(num1,num2):
    return num1 ** (1.0/num2)

while True:

    print('Select the Function')
    print('1. Addition -> x + y')
    print('2. Subtract -> x - y')
    print('3. Multiply -> x * y')
    print('4. Divide -> x / y')
    print('5. Power -> x^y')
    print('6. Square Root -> x^(1/y)')
    print('7. Quit')

    user = raw_input('> ')
    num1 = raw_input('Num1: ')
    num2 = raw_input('Num2: ')

    if user == '1':
        print
        print(str(num1) + " + " + str(num2) + " = " + str(add(int(num1),int(num2))))
        print
    elif user == '2':
        print
        print(str(num1) + " - " + str(num2) + " = " + str(int(num1),int(num2)))
        print
    elif user == '3':
        print
        print(str(num1) + " x " + str(num2) + " = " + str(mult(int(num1),int(num2))))
        print
    elif user == '4':
        print
        if num2 == '0':
            print('#DIV/0! Error: Num2 cannot be 0')
        else:
            print(str(num1) + " / " + str(num2) + " = " + str(div(int(num1),int(num2))))
        print
    elif user == '5':
        print
        print(str(num1) + " squared by " + str(num2) + " = " + str(sq(int(num1),int(num2))))
        print
    elif user == '6':
        print
        print(str(num1) + " square root by " + str(num2) + " = " + str(sqrt(int(num1),int(num2))))
        print
    else:
        print('Quitting')
        time.sleep(2)
        break


    
    
