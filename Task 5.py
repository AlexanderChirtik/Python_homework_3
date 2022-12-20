# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(x):
    if (x == 1 or x == 2):
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

def nega_fibonacci(x):
    if x == 1:
        return 1
    elif x == 2:
        return -1
    else:
        value_1 = 1
        value_2 = -1
        for i in range(2, x):
            value_1, value_2 = value_2, value_1 - value_2
        return value_2

list = [0]
number = int(input("Введите число "))
for i in range(1, number + 1):
    list.append(fibonacci(i))
    list.insert(0, nega_fibonacci(i))
print(list)
