#simple CALCULATOR by DM-BOYZ

print("\033[1;36m  ==============")
print("\033[1;33m  | CALCULATOR |")
print(" \033[1;34m ==============")


number1 = input('\033[1;36mEnter a number: ')
number2 = input('\033[1;35mEnter the other number: ')
logo = ''' \033[1;31m1. + \n 2. - \n 3. * \n 4. / \n '''
print logo
chose = input('\033[1;33mchose sign: ')
if chose == 1:
    print '\033[1;32mYour Result is :',number1+number2
elif chose == 2:
    print number1-number2
elif chose == 3:
    print number1*number2
elif chose == 4:
    print number1/number2
else:
    print 'wrong input'