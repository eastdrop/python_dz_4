# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте
# выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

N = int(input())
s = []
for i in range(N):
    num = int(input())
    s.append(num)
print(s)
max_a = 0
if N == 1:
    max_a = s[0]
if N == 2:
    max_a = s[0] + s[1]
if N == 3:
    max_a = s[0] + s[1] + s[2]
if N > 3:
    for i in range(N):
        var = 0
        if i == 0:
            var = s[i] + s[-1] + s[i+1]
            if var > max_a:
                max_a = var
        elif i == len(s) - 1:
            var = s[i] + s[i - 1] + s[1]
            if var > max_a:
                max_a = var
        else:
            var = s[i] + s[i - 1] + s[i + 1]
            if var > max_a:
                max_a = var
print(max_a)
