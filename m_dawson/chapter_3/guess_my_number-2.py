# Программа 'Угадай число' с 5 попытками

import random



print("\n\n\tДобро пожаловать в игру 'Отгадай число'!")
print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
print("У вас есть только 5 попыток, чтобы угадать число.\n")

# Начальные значения
the_number = random.randint(1, 100)
guess = 0
tries = 0

# Цикл отгадывания
while tries < 5:
  guess = int(input("Ваше предложение: "))
  tries += 1

  if guess == the_number:
    print(f"Вам удалось угадать число! Это в самом деле {the_number}")
    print(f"Вы затратили на отгадывание {tries} попыток\n")
    tries = 5
  elif guess > the_number:
    print(f"Меньше. Осталось попыток: {5 - tries}")
  else:
    print(f"Больше. Осталось попыток: {5 - tries}")

if tries == 5 and guess != the_number:
  print(f"Ты неудачник! Игра окончена. Загаданное число было: {the_number}")
