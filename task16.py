# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
import random

n = int(input("Введите колл элементов в масиве: "))
x = int(input("Введите число поиска: "))
temp = []
count = 0
for i in range(n):
    temp.append(random.randint(0, 5))
    if temp[i] == x:
        count +=1
print(temp)
print('Число', (x), 'встречается' 'в массиве', (count), 'раз.')

