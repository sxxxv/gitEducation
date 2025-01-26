# Программа Киндерсюрпиз
# Демонстрирует генерацию случайного подарка из 5 возможных

import random


print("\n\n\tПеред вами Киндер сюрприз. \n\tОткрыв его вы получаете случайную фигурку из коллекции Черепешек-ниндзя.\n")

# Создаем переменные с подарками
gift1 = "splinter"
gift2 = "leonardo"
gift3 = "michelangelo"
gift4 = "raphaello"
gift5 = "donatelo"

# Создаем случайное число в диапазоне от 1 до 5
gift = random.randint(1, 5)

# Создаем условие показывающее подарок в зависимости от выпавшего числа
if gift == 1:
  print("Вы получили :", gift1)
elif gift == 2:
  print("Вы получили: ", gift2)
elif gift == 3:
  print("Вы получили: ", gift3)
elif gift == 4:
  print("Вы получили: ", gift4)
else:
  print("Вы получили: ", gift4)

input("\nНажмите Enter, чтобы выйти.")

