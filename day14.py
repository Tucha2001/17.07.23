#problem 1
# def calculate(number):
#     square = number ** 2
#     return square
# number = int(input('>>>'))
# print(calculate(number))



# problem 2
# import random
# def generate_random_numbers():
#     random_numbers = []
#     for i in range(10):
#         random_numbers.append(random.randint(0,100))
#     return random_numbers
# generate_random_numbers()
# print(generate_random_numbers())


# problem 3
# def reverse_s(string):
#     return string[::-1]
# print(reverse_s('Bekarys'))




# problem 4
# def sum_calculator(massive):
#     sum = 0
#     for  i in massive:
#        sum+=i
#     return sum
# massive = [5,10,15,20,25]
# print(sum_calculator(massive))




# problem 5
# def palindrome(string):
#     return string == string[::-1]
# print(palindrome('KazaK'))
# print(palindrome('Kazakhstan'))




def translation(numbers):

numbers = int(input('>>>'))
binary = ''
while numbers > 0:
    binary = str(numbers%2)+binary
    numbers = numbers // 2
print(binary)
return 

print(translation(numbers))


 

        


