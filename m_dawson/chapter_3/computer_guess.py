# Игра 'Компьютер угадывает число'

def computer_guess():
  print("Загадай число от 1 до 100 (держи его в уме, не говори компьютеру.)")
  input("Нажми Enter, когда будешь готов.")

  # Устанавливаем границы
  minimum = 1
  maximum = 100
  attempts = 0

  while True:
    # Компьютер делает предложение
    guess = (minimum + maximum) // 2
    attempts += 1

    print(f"\n\nКомпьютер думает, что твое число {guess}")
    feedback = input("Ответь: 'больше', 'меньше' или 'угадал': ").lower()

    if feedback == "угадал":
      print(f"\nУра! Компьютер угадал твое число за {attempts} попыток.")
      break
    elif feedback == "больше":
      minimum = guess + 1
    elif feedback == "меньше":
      maximum = guess - 1
    else:
      print("\nПожалуйста, отвечай только 'больше', 'меньше' или 'угадал'")

# Запускаем игру
computer_guess()
