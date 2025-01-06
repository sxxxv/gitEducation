# Кости
# Депонстрирует генерацию случайных чисел

import random

#Создаем случайные числа в диапозоне 1 - 6
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1
total = die1 + die2

print("При впшем броске выпало", die1, "и", die2, "очков. В сумме", total)
input("\n\nНажмите Enter, чтобы выйти.")
