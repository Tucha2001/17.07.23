# problem 9
count_condition_1 = 0
count_condition_2 = 0


numbers = range(-100, 101)

for number in numbers:
    
    if number % 13 == 0 and number % 2 == 0:
        number = number ** 2
        count_condition_1 += 1

    
    if number % 7 == 0 and number % 2 != 0:
        count_condition_2 += 1
        if number % 2 != 0:
            print(number)
print("Количество чисел, подходящих под первое условие:", count_condition_1)
print("Количество чисел, подходящих под второе условие:", count_condition_2)






# number = []
# for i in range(-101,101):
#     if i % 13 == 0:
#         if i % 2 == 0:
#             number.append(i)
        
#     if i >= 7:
#         if i % 3 == 0:
#             number.append(i)
# print(number)


# #problem 8
# list = [1023,201,496,365]
# for i in list():
#     if 100 <= list <= 999:
#         print('Это число трехзначтное')
#     else:
#         print('число не трехзначтное')
#     if list > 0 and list%2 ==0:
#         print('Это число положительное и четное')
#     else:
#         print('Это число не положительное и не четное')
#     if list / 31 == 0:
#         print('Это число делится на 31 без остатка')
#     else:
#         print('Это число не делится на 31 без остатка')

#     if list > 100 and list %17 == 0: 
#         print('удолитвар ')
#     elif list > 150 and list == 13**2:
#         print('Что это за число')
# print(list)


# problem 7
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in range(len(names)):
#     if i%2 >= 1:
#         print(names[i])



#problem 6-1
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)




# for i in range(len(names)):
#     if i%2 == 0:
#         print(names[i])



#problem - 6
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in names:
#     if names.index(i)%2 == 0:
#         print(i)


#problem -4
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     print(languages.index(i),i)
    



#problem-3
# a = 7
# for i in range(5):
#     a *= a
#     print(a)


# problem 2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == 'php':
#         break
#     print(i)
    



#problem 1.1-1.11
# a = []
# for i in range(1,11):
#     print(i)

# a = []
# for i in range(1,21):
#     if i%2 == 0:
#         print(i)


# a = 0
# for i in range(1,101):
#     a += i
#     print(a)
    

# for i in range(1,11):
#     a = i * 5
#     print(a)

# a = 1
# for i in range(1,6):
#     a*=i
#     print(a)


# for i in ('Hello,World! '):
#     print(i)


# a = 0
# for i in [1,2,3,4,5]:
#     a+=i
#     print(a)



# num = [1,2,3,4,4,5]
# new_list = []
# for i in num:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


# for i in range(10,0,-1):
#     print(i)


# list = []
# for i in range(1,101):
#     if i%3 == 0 and i%5 == 0:
#         list.append(i)

# print(list)

    
# problem-1
# lang1 = 'rust'
# languages = ['go','java','php','python','javascript','ruby']
# if lang1 in languages:
#     print('this languages is in list')
# else:
#     print('No')




# s = []
# for i in range(5):
#     print(i)
#     num = int(input('Enter: '))
#     s.append(num)
# print(s)

