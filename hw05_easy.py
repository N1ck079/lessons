# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

source = [1, 2, 4, 0]
a = [i ** 2 for i in source]
print(a)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list1 = ["banana", "apple", "orange", "grape", "melon"]
list2 = ["grape", "citron", "apple", "pineapple"]
result = [fruit for fruit in list1 if fruit in list2]
print(result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
source = [random.randint(-100, 100) for i in range(10)]
target = [itm for itm in source if not itm % 3 and itm > 0 and itm % 4]
print(f"source = {source}")
print(f"target = {target}")