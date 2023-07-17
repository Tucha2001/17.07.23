#5 Problem
While  True:    
a = input("Введите 1 что бы ввойти или  2 что бы зарегестироватся: ")
if a == "1" :
    log = input("Введите логин: ")
    pas = input("Пароль:")  
    with open('database.txt', 'r') as f:
            data = f.read()
            if log in data and pas in data:
                print("Вы успешно вошли")
            else:
                print("Зарегайтесь")
elif a == "2":
        log2 = input("Ввеидте логин:")
        pas2 = input("Ввдите парль:")
        pas3 = input("Введите еще раз пароль:")
        if pas2 == pas3:
            with open('database.txt', 'r') as f:
                data = f.read()
                if log2 in data and pas2 in data:
                    print("Вы уже зареганы")
                else:
                    with open('datase.txt', 'a') as f:
                        f.write(f"{log2} {pas2}")
                        print("Вы успешно зреганы")
    
#problem 4
# with open ('python.txt','r') as file:
#     t_words = [] 
#     text = file.read()
#     words = text.split()
#     for word in words:
#         if 't' in word or 'T' in word:
#             t_words.append(word)
    
    
#     print(t_words)



#problem 3
# with open ('users.txt','r') as file:
#     text = file.read()
#     if 'w' in text:
#         print('Да, в тексте есть w')
#     else:
#         print('Нет, в тексте нет w')



# problem 2
# with open('users.txt','a') as file:
#     login = input('LOGIN: ')
#     password = input('PASSWORD: ')
#     file.write(f'{login},{password}')

# problem 1
# with open('directories.txt','r') as file:
#     text = file.read()
#     print(text)




# with ('main.txt', 'a') as file:
#     for i in range(1, 101):
#         file.write(f'{i} \n')







#////////////////////////////////////////////////////////////////////////////////
# f = open('main.txt', 'r')
# text = f.read() # фаил открыт в режимах чтения и запаковки в переменновой text 
# f.close()
# print(text)


# f = open('main.txt', 'a')
# f.write('Hello world!\n')
# f.close()

# a = 'Hello world!\n'

# with open('main.txt', 'a') as file:
#     file.write('Hello world!\n')

# with open('main.txt', 'r') as file:
#     text = file.read()
#     print(len(text.split('\n')))