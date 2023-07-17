
# problem 1
# parameters = (lambda x,y,z: x*y*z)(2,3,4)
# print(parameters)
#/////////////////////////////////////////
# a = lambda x,y,z:f'{x*y*z}'
# print(a(2,3,4))


# problem 2
# day = (lambda x,y : x-y)(365,200)
# print('До Нового года осталось',day,'дней')


# problem 3
# def odd_numbers(n):
#     if n <= 0:
#         return
#     if n % 2 != 0:
#         print(n)
#     odd_numbers(n - 1)

# odd_numbers(10)


# problem 4
# def remove_elements(s):
#     if len(s) == 0:
#         return
#     s.pop()
#     print(s)
#     remove_elements(s)

# # Пример использования функции
# my_set = {1, 2, 3, 4, 5}
# remove_elements(my_set)