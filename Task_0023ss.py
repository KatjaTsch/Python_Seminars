# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

stroka = input()
d={}
for i in stroka:
    d[i]= d.get (i,0)+1

for k,n in d.items():
    print (f'{k}_{n}')

# for symbol in string:
#     if symbol not in dict:
#         dict[symbol] = 1
#     else:
#         dict[symbol] +=1
# for key, value in dict.items():
#     print(f'{key}_{value}')