
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





# problem 3-3
# data_list = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
# s = list(map(lambda x:x*1.185, data_list))
# print(s)



# # decarator
# def decorator(func):
#     def wrapor():
#         list = []
#         for i in func():
#             list.append(i*1.185)
#         return list
#     return wrapor 
# @decorator    
# def main():
#     return [1745345, 98726, 439872634, 7312, 64872, 123687126, 9312, 4124, 231, 3123, 34, 3453]
# print(main())


# def decorator(func):
#     def all_data():
#         list = []




def input_decorator(func):
    def wrapper(data):
        print('start')
        func(data)

    return wrapper


@input_decorator
def process_data(data):
    print("Вы ввели:", data)



data = input("Введите данные: ")
process_data(data)

