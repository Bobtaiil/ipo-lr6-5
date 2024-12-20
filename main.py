
#Написать программу, которая:
#- Создаёт с помощью генератора списков, список случайных целых чисел от -50 до 50 размером 25 элементов.
#- Находит количество положительных, отрицательных и нулевых элементов в списке.
#- Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
#- Выводит самое большое и самое маленькое значение

#Импортируем модуль random
import random

#Создаём список случайных целых чисел
random_numbers = [random.randint(-50, 50) for _ in range(25)]

#Счётчик кол-ва положительных элементов
positive_count = 0
#Перебор значений Random_numbers
for num in random_numbers:  
    #Если число больше нуля Счётчик положительных чисел увеличивается на 1
    if num > 0:
        positive_count += 1
        
#Счётчик отрицательных чисел
negative_count = 0
#Перебор значений random_numbers
for num in random_numbers: 
    #Если число меньше нуля Счётчик отрицательных чисел увеличивается на 1
    if num < 0:
        negative_count += 1

#Счётчик нулей
zero_count = 0
#Перебор значений random_numbers
for num in random_numbers: 
    #Если число равно нулю Счётчик нулевых чисел увеличивается на 1
    if num == 0:
        zero_count += 1

#Кол-во значений random_numbers
all_count = len(random_numbers)

#Процент положительных
percent_positive = (positive_count / all_count) * 100
#Отрицательных
percent_negative = (negative_count / all_count) * 100
#Нулей
percent_zero = (zero_count / all_count) * 100

#Наивысшее значение
max_value = max(random_numbers)
#Наименьшее
min_value = min(random_numbers)

#Наш список чисел
print("Список случайных чисел:", random_numbers)
#Положительные
print("Положительные:", positive_count, f"({percent_positive:}%)")
#Отрицательные
print("Отрицательные:", negative_count, f"({percent_negative:}%)")
#Нули
print("Нули:", zero_count, f"({percent_zero:}%)")
#Наивысшее
print("Наивысшее значение:", max_value)
#Наименьшее
print("Наименьшее значение:", min_value)