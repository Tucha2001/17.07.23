# users = {
#     'name': 'Anton'
# }
# try:
#     print('users',['name'])

# except KeyError as e:
#     print('Мы отлавили KeyError',e)

# except NameError as e:
#     print('Вы не создали переменную',e)

# else:
#     print('Все ок! 200')

# finally:
#     'обработка ошибок завершено!'


zero_except = 0
while True:
    try:
        print(eval(input('>>> ')))
        
    except ZeroDivisionError as e:
        zero_except += 1
        print('Вы пытаетесь делит на ноль!')
        print('больше не пытайтес! или мы вас забаним')
    
    except TypeError as e:
        print('Вы пытаетесь работать с разынми типами данных!',e)
    

    except KeyboardInterrupt as e:
        print('\n Вы остановили операцию!')
        break

    except SyntaxError as e:
        print('Синтаксическая ошибка')

    except NameError as e:
        print('Вы не создали перемнное')

    if zero_except == 3:
        print('Мы вас забанили из заZeroDivisionError')
        print('ВЫ уже подедили 3 раза')
        break