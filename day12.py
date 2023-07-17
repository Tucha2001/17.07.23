# #problem 1
# import random
# a = random.randint(0,10)
# try:
#     user = int(input(">>> "))
#     if user == a:
#         print('you win')
#     else:
#         print('you utyl')
# except ValueError as e:
#     print('vy peredali vmesto string')

# problem 2
# from random import choice
# company = ['Iphone','Samsung','LG','Oppo','Nokia']
# print(choice(company))


#problem 3
# import random
# a = random.randint(1,1000)

# while True:
#     try:
#         user = int(input('Введите число: '))
#         if user < a:
#             print('слишком мало')
#         elif user > a:
#             print('слишком много')
#         else:
#             print('числы равны')
#             break
#     except ValueError as e:
#         print('Вы предали в место string')


# problem 4
# import random
# try:
#     numbers = [12,62,32,49,9,7,3,95,84,1,354]
#     a = random.choice(numbers)
#     print(a)
# except ValueError as e:
#     print('Не целое число')


#problem 5
# import random
# a= random.random()
# b = random.random()
# print(a,'a')
# print(b,'b')



# # problem 6
# import random
# my_list= [25,65,8,7,6,97,'I am Kazakh',{'country': 'Kazakhstan','city':'Almaty'}]
# try:
#   my_random = random.choice(my_list)
#   print(my_random)
# except IndexError:
#   print('список пустой')
# except IndexError:
#   print('несовместной тип данных')



import random
n = int(input('>>>'))
try:
  
    a  = random.randint(1,n)
    if a > 0:
        print("Случайное число от 1 до",a)
except ValueError:
    print('error')
    


# import random

# def generate_random_number(n):
#     try:
#         n = int(n)
#         if n <= 0:
#             raise ValueError("Число должно быть целым положительным.")
#         random_number = random.randint(1, n)
#         return random_number
#     except ValueError as e:
#         print("Ошибка:", e)

# input_number = input("Введите число: ")
# random_number = generate_random_number(input_number)
# if random_number is not None:
#     print("Случайное число от 1 до", input_number, ":", random_number)