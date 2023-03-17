# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

A = []
from random import randint
n = int(input("Введите размер массива: "))
min_num = int(input("Введите min: "))
max_num = int(input("Введите max: "))
A=[randint(min_num, max_num) for i in range(n)]
print(A)

for i in range(len(A)):
    if min_num <= A[i] <= max_num:
        print(i)