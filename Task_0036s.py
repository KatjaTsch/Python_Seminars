# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284

# def SumOfDividers(x):
#     sum = 0
#     for i in range (1, x//2+1):
#         if x%1 == 0:
#             sum +=i
#     return sum

# k = (int(input('Введите: ')))
# print (SumOfDividers(k))

# for n in range(k):
#     # for m in range(n+1, k):
#     j = SumOfDividers(n)
#         # if SumOfDividers(n) == m and SumOfDividers(m) == n:
#     if n < j and n<k and n == SumOfDividers(j):  
#         print(n, j) 





n = int(input())
list_1 = list()
for i in range(n):
    summa = 0
    for j in range(2, i//2+1):
        if i % j ==0:
            summa += j
    list_1.append(tuple([i, summa]))
print(list_1)

for i in range(len(list_1)):
    for j in range(i, len(list_1)):
        if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
            print(*list_1[i])