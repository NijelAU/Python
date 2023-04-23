# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
#  и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def result (num, degree):
    if degree == 1:
        return num
    if degree != 1:
        return num * result(num, degree-1)
    

num = int(input('Введите число  - '))
degree = int(input('Введите степень числа - '))

print("Результат = ", result(num, degree))