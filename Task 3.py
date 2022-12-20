# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
list = []
for i in range(random.randint(3, 6)):
    list.append(round(random.uniform(-5, 5), 3))
print(list)
index = 0
list2 = []
while (len(list) > index):
    value = list[index] * 1000
    if (list[index] > 0):
        value = value % 1000
    else:
        value = (value % -1000) * -1
    list2.append(value)
    index += 1
result = max(list2) - min(list2)
print(result / 1000)