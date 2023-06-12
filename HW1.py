# =====================================================================
# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
"""
print("===== С У М М А   Ц И Ф Р    Ч И С Л А =========")
number = int(input("Введите трёхзначное натуральное число: "))

digitsSumm = number % 10 + (number // 10) % 10 + (number // 100) % 10
print("ОТВЕТ: сумма цифр данного числа равна", digitsSumm)
"""

# =====================================================================
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

"""
print("\n==== РАСЧЁТ ЖУРАВЛИКОВ ПО КАЖДОМУ ИГРОКУ ====")
total = int(input("Введите общее количество "))
# Петя и Серёжа сделали по Х журавликов, вместе - 2Х, Катя = 4Х
# 2Х + 4Х = total
# X = total / 6
if total % 6 == 0:
    print(f"ОТВЕТ: Петя и Серёжа сделали по {total // 6} журавл., а Катя - {4 * total // 6}. Всего - {total}.\n")
else:
    print("ОТВЕТ: При таких вводных данных задача целого решения не имеет.\n")
"""

# =====================================================================
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

"""
print("\n==== П О И С К   С Ч А С Т Л И В О Г О   Б И Л Е Т А ====")

flag = True
while (flag):
    ticketNumber = input("Введите шестизначный номер билета для проверки: ")
    if len(ticketNumber) == 6:
        ticketNumber = int(ticketNumber)
        flag = False

leftPart = ticketNumber // 1000
rightPart = ticketNumber % 1000

leftPartDigitsSum = leftPart % 10 + (leftPart // 10) % 10 + (leftPart // 100) % 10
rightPartDigitsSum = rightPart % 10 + (rightPart // 10) % 10 + (rightPart // 100) % 10

if leftPartDigitsSum == rightPartDigitsSum:
    print("ПОЗДРАВЛЯЮ! Ваш билет счастливый! Можете его съесть. Приятного аппетита :)\n")
else:
    print("УВЫ ... Вам попался обычный билет. Повезёт в другой раз (НИКОГДА).\n")
"""

# =====================================================================
# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
print("\n==== Л О М А Е М   Ш О К О Л А Д К У ====")

length = int(input("Введите размеры шоколадки: длину... ")) 
width  = int(input("                          ширину... "))
part   = int(input("Сколько кусочков хотим отломить?... "))

if part == length*width:
    print("\nПравильно! Чего её ломать? Надо брать ВСЮ ЦЕЛИКОМ!\n")
elif part > length*width:
    print("\nНЕ ВЫЙДЕТ! Куска больше, чем вся шоколадка не отломить!\n")
elif (part % length == 0 or part % width == 0):
    print("\nОтломить за 1 раз такой кусочек ВОЗМОЖНО! Приятного аппетита ^_^\n")
else:
    print("\nК сожалению такой кусочек от шоколадки за 1 раз отломить НЕЛЬЗЯ >_<\n")