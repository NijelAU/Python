# # Задача №3. Решение в группах
# # В некоторой школе решили набрать три новых
# # математических класса и оборудовать кабинеты для
# # них новыми партами. За каждой партой может сидеть
# # два учащихся. Известно количество учащихся в
# # каждом из трех классов. Выведите наименьшее
# # число парт, которое нужно приобрести для них.
# # Input: 20 21 22(ввод чисел НЕ в одну строку)
# # # Output: 32

a=int(input("введите колличество учеников в классе№1 "))
b=int(input("введите колличество учеников в классе№2 "))
c=int(input("введите колличество учеников в классе№3 "))
# print(a//2+b//2+c//2+a%2+b%2+c%2)
# a = 20
# b = 21
# c = 22

# int full = (a + b + c + 1)//2
# print(full)
# if (a % 2 ==0):
#     a1 = a / 2
# else:
#     a1 = a / 2 + 1
# if (b % 2 ==0):
#     b1 = b / 2
# else:
#     b1 = b/ 2 + 1
# if (c % 2 ==0):
#     c1 = c / 2
# else:
#     c1 = c / 2 + 1
# print(int( a1 + b1 +c1))
print((a + 1) // 2)
print((b + 1) // 2)
print((c + 1) // 2)
print ((a+1)//2+(b+1)//2+(c+1)//2)