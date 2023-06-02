# Урок 3. Списки и словари
# =====================================================================================
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# import random

# sizeArray = int(input("Введите длину массива... "))
# arrayOfNatural =  list()

# print("Сгенерированный массив:")
# for i in range(sizeArray - 1):
#     arrayOfNatural.append(random.randint(10, 20))
# print(arrayOfNatural)

# number = int(input("Посчитаем сколько раз в массиве встречается ЧИСЛО ... "))
# print(f"ОТВЕТ: ЧИСЛО {number} встречается в массиве {arrayOfNatural.count(number)} раз.\n")

# temp = str(arrayOfNatural)
# number = int(input("Посчитаем сколько раз в массиве встречается ЦИФРА ... "))
# print(f"ОТВЕТ: ЦИФРА {number} встречается в массиве {temp.count(str(number))} раз.\n")

# =====================================================================================
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному 
# числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

# import random

# sizeArray = int(input("Введите длину массива... "))
# arrayOfNatural =  list()

# print("Сгенерированный массив:")
# for i in range(sizeArray - 1):
#     arrayOfNatural.append(random.randint(10, 20))
# print(arrayOfNatural)

# userNumber = int(input('Введите число для поиска ближайшего по значению... '))
# nearest = arrayOfNatural[0]
# minDiff = abs(userNumber - arrayOfNatural[0])

# for i in range(1, len(arrayOfNatural)):
#     diff = abs(arrayOfNatural[i] - userNumber) 
#     if diff <= minDiff: 
#         nearest = arrayOfNatural[i]
#         minDiff = diff
        
# print(f'Ближайшее к числу {userNumber} по значению будет {nearest}')

# =====================================================================================
# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного 
# пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо 
# только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12

word = input("Введите слово, подсчитаем его ценность: ").upper()

dict = {'AEIOULNSTRАВЕИНОРСТ':1,
        'DGДКЛМПУ':2,
        'BCMPБГЁЬЯ':3,
        'FHVWYЙЫ':4,
        'KЖЗХЦЧ':5,
        'JXШЭЮ':8,
        'QZФЩЪ':10}

result = 0

for letter in word:
    for key,value in dict.items():
        if letter in key:
            result += value

print(f'Ценность Вашего слова составляет {result} баллов.')