# #  problem 1-1
# import random 
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random_names = random.sample(names, 4)
# print(random_names)

# problem 2
# import sys
# print(sys.version)

# problem 3
# import sys
# print(sys.argv)


#problem 4
# import os
# import random
#####os.system('mkdir weekend')
# files = ['family.txt','friends.txt','girls.txt','university.txt','school.txt']
# for i in files:
#     os.system(f'touch weekend/{i}')


# problem 5
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random.shuffle(names)
# group1 = names[:3]
# group2 = names[3:6]
# group3 = names[6:9]
# group4 = names[9:]
#
# print("Группа 1:", group1)
# print("Группа 2:", group2)
# print("Группа 3:", group3)
# print("Группа 4:", group4)


import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
random.shuffle(names)
t1 = []
t2 = []
t3 = []
t4 = []
for i in (t1,t2,t3,t4):
    for _ in range(3):
        i.append(names.pop(random.randint(0, len(names)-1)))
print(t1)
print(t2)
print(t3)
print(t4)


# problem list 2-1
# import sys
# print(sys.argv)


# problem 3
# import sys
# a = int(input('>>>'))
# b = int(input('>>>'))
# if a > b:
#     print('a больше sys')
# else:
#     print('b больше sys')

# problem 4
# import random
# import string

# def generate_password(length):
    
#     password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
#     return password

# N = int(input("Введите число N для генерации пароля: "))
# password = generate_password(N)


# print("Сгенерированный пароль:", password)
