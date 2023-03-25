
def Change(data, number):
     with open('file.txt', 'w', encoding='utf-8') as file:
         file.write(f'{data} : {number} \n')
# data = input('введите имя: \n')
# number = input('введите телефон: \n')
# Change(data, number)