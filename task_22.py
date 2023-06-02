# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем
# пользователь вводит сами элементы множеств.

s1 = []
n = int(input())
for i in range(n):
    number = int(input())
    s1.append(number)
s1 = set(s1)
print(s1)

s2 = []
n = int(input())
for i in range(n):
    number = int(input())
    s2.append(number)
s2 = set(s2)
print(s2)
s1 = list(s1)
s2 = list(s2)
s3 = s1 + s2
check = []
for i in set(s3):
    if s3.count(i) > 1 and i not in check:
        check.append(i)
print(check)
