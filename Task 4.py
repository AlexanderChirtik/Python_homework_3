# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

value = int(input("Введите число "))
i = 1
binary = 0
while (value > 0):
    binary += (value % 2) * i
    if (value % 2 == 0):
        value = value / 2
    else:
        value = (value / 2) - 0.5
    i *= 10
list = str(binary).split('.')
print(list[0])