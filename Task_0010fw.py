# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи,
# выведите число -1.

n = int(input('Введите искомое число:'))

prev_num = 0
current_num = 1
temp = None
count = 0
while prev_num <= n:
    count += 1
    if n == prev_num:
        print(count)
        break
    temp = prev_num
    prev_num = current_num + prev_num
    current_num = temp
else:
    print("Число не является числом Фибонначи")