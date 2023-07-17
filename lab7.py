sentence = input("Введите предложение: ")
a = sentence.split()
length1 = len(sentence[0])
list = []
for sentence in a:
    if len(sentence) > length1:
        list.append(sentence)
    if list:
        print("Слова, содержащие больше букв, чем первое слово:")
        for sentence in list:
            print(sentence)
    else:
        print("В предложении нет слов, содержащих больше букв, чем первое слово.")
list(sentence)











# 4-2 Создать Дебильный Калькулятор
#         Который будет запрашивать у пользователя один из выражений (+,-,/,*,**, //,%)
#         После он должен спросить первую цифры за тем вторую .
#         В зависимости от того что выбрал пользователь Необходимо совершить выражение и показать ответ

#         Пример:
#         Первую цифру: 6
#         Пользователь выбирает : *
#         Вторую цифру: 5
#         Ответ: 6 * 5 = 30

# num1 = float(input('Введите1: '))
# num2 = float(input('Введите2: '))

# while True:
#     a = input("Выберите операцию  или введите 'stop' для выхода: ")
#     if a == 'stop':
#         print('Good Bye')
#         break
#     if a not in a:
#         print('ERROR,NOCORECCT')

#     if  a == '+':
#         print(num1+num2)
#     elif a == '-':
#         print(num1-num2)
#     elif a == '*':
#         print(num1*num2)
#     elif a == '**':
#         print(num1**num2)
#     elif a == '/':
#         if num2 == 0:
#            print('error')
#         else:
#            print(num1/num2)
#     elif a == '//':
#         print(num1//num2)
#     elif a == '%':
#         print((num1*num2)/100)









#8-1 Создайте список чисел от 1 до 20. Выведите только числа, которые делятся на 2 и не делятся на 3.
# list = []
# for i in range(1,21):
#     if i%2 ==0 and i%3 != 0:
#         print(i)



#7-2 Попросите пользователя ввести предложение. Выведите каждое слово в верхнем регистре.
# i = input('Введите предложение: ')
# print(i.upper())
