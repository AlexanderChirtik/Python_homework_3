# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

list = []
for i in range(random.randint(3, 6)):
    list.append(random.randint(-9, 9))
print(list)

new_list = []
index = 0
while(len(list) / 2 > index):
    new_list.append(list[index] * list[len(list) - index - 1])
    index += 1
print(new_list)

