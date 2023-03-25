# Задача 38: Дополнить телефонный справочник возможностью 
# изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал
# для изменения и удаления данных.
# data = input('введите имя: ')
# number = input('введите номер: ')

# def Change(data, number):
Delite = 'file.txt'
try:
    with open(Delite, 'r+') as f:
        f.truncate()
except IOError:
    print('Failure')

# Change(data, number)
# def Del(data, number):
#     with open('file.txt', 'r', encoding='utf-8') as file:
#         # flag = False
#         for line in file:
#             if data in line:
#                 with open('file.txt', 'w+', encoding='utf-8') as file:
#                     file.write(f' {data} \n')
#                 print(line)
#             if number in line:
#                 with open('file.txt', 'w+', encoding='utf-8') as file:
#                     file.write(f' {data} \n')
#                 print(line)
        #         flag = True
        # if flag == False:
        #     print('\n Не найдено! \n')
# Del('536')


# choise = int(input('Введите данные для изменения: \
#     \n 1 - изменить фамилию \n 2 - изменить номер телефона'))
# match choise:
#     case 1:


# input('Введите данные для изменения: \n')
# def Change(data, number):
#     with open('file.txt', 'w', encoding='utf-8') as file:
#         file.write(f'{data} : {number} \n')
# data = input('введите данные: \n')
# number = input('введите данные: \n')
# Change(data, number)