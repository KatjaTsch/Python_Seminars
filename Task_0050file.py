# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# 1) Добавить
# 2) Вывести всех
# 3) Поиск по фамилии

def Input(data, number):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data} : {number} \n')


# def OutputAll():

#     with open('file.txt', 'r', encoding='utf-8') as file:
#         for line in file:
#             print(line)
       


# def Search(data):
#     data = data.lower()
#     with open('file.txt', 'r', encoding='utf-8') as file:
#         flag = False
#         for line in file:
#             if data in line.lower():
#                 print(line)
#                 flag = True
#         if flag == False:
#             print('\n не найдено \n')
