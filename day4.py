# formula okruzhnosti
# from math import pi
# r = int(input('Введите: '))
# pi = 3.14
# S = pi * r
# print(S)
# d = 2*pi*r
# print(d)

# Pifagor
# from math import sqrt
# a = int(input('input1: '))
# b = int(input('input2: '))
# c = sqrt(a**2 + b**2)
# print(c)

# CALCULATOR
num1 = float(input('Введите1:'))
num2 = float(input('Введите2: '))
a = input('введите: ')
if a == '+':
    print(num1+num2)
elif a == '-':
    print(num1-num2)
elif a == '*':
    print(num1*num2)
elif a == '**':
    print(num1**num2)
elif a == '/':
    if num2 == 0:
        print('error')
    else:
        print(num1/num2)
elif a == '//':
    print(num1//num2)
elif a == '%':
    print((num1*num2)/100)


# //////////////
# a = 'hello world world hello'
# mid = len(a) // 2
# b = a[:mid][::-1] + a[mid:]
# print(b)