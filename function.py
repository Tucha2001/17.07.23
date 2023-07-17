# def hello():
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')


# for i in range(10):
#     print(i)
#     hello()


# def get_len(text: str) -> int:
#     count = 0
#     for _ in text:
#         count += 1
#     return count


# s = 'kashdkjgashjdjhashdcjhgcagjcasxghashkxcakshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# d = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'


# count = 0
# for i in s:
#     count += 1

# count_b = 0
# for i in b:
#     count_b += 1

# s_len = get_len(s)
# b_len = get_len(b)
# d_len = get_len(d)

# print(s_len == s_len == d_len)

# import string
# import random


# def generate_password(length: int) -> str:
#     symbols = string.ascii_letters + string.digits
#     password = ''
#     for _ in range(length):
#         password += random.choice(symbols)
#     return password


# p1 = generate_password(10) 
# p2 = generate_password(10) 
# p3 = generate_password(10) 
# p4 = generate_password(10) 
# print(p1,p2,p3,p4)







# def get_5(item: int, massiv: list) -> bool:
#     if type(massiv) not in [list, tuple]:
#         raise TypeError('Массив должен быть списком или картежом')
    
#     if item in massiv:
#         return True
#     return False

# print(get_5(2, 6))