''' MM to In Converter v0.7 '''

print('Welcome to Conversion of MM to IN')
print('Press X to stop')

conv = 0.0394

while True:
    user1 = raw_input('Number #1: ')
    user2 = raw_input('Number #2: ')
    if user1 >= 0 and user2 >= 0:
        num1 = float(user1) * float(conv)
        num2 = float(user2) * float(conv)
        print
        print("  "+str("{0:.2f}".format(round(num1,2))+" in"))
        print("  "+str("{0:.2f}".format(round(num2,2))+" in"))
        print
        print('Area? Press any Key or X ')
        user3 = raw_input('> ')
        print
        if user3 == 'x' or user3 == 'X':
            break
        else:
            num3 = num1 * num2
            print("  "+str("{0:.2f}".format(round(num3,2))+" in^2"))
            print
    else:
        print('Enter the Positive Numbers only!!')
