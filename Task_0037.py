# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести 
# с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

A = []
n = int(input("Введите количество элементов: "))
A = [0]*n
A[0] = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))

for i in range(1, n):
    A[i] = (A[0] + (n-1)*d)
print(A)



# A[ for i in range(n)]
# print(A)

# for i in A:
#     if a+A[i+1]+A[i+2] > max:
#         max = a
# print(max)

# int[] GetArray(int size, int minValue, int maxValue)
# {
#     int[] rez = new int[size];

#     for(int i = 0; i < size; i++)
#     {
#         rez[i] = new Random().Next(minValue, maxValue+1);
#     }
#     return rez;
# }

    