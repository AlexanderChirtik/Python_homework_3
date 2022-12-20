# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
import random

list = []
for i in range(random.randint(5, 10)):
    list.append(random.randint(-9, 9))
print(list)
index = 0
sum = 0
while (len(list) > index):
    sum += list[index]
    index += 2
print(sum)