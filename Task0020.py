# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

A = []
from random import randint
N = int(input("Введите число элементов массива: "))
A=[randint(0, 5) for i in range(N)]
print(A)


X = int(input("Введите искомое число: "))
count = 0
for i in range(0, len(A)):
    if A[i] == X:
        count += 1
print(f"число {X} встречается {count} раз")


# for i in range(N):
#     A.append(i)
# print(A)

# A = [int(i) for i in input().split()]
# print(A)
# X = int(input())
# print(A.count(X))
# for i in range(0, len(N)-1):
#     print(A[N])
