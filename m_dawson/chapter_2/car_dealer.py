# Программа автодилер
# Расчитывает полную стоимсоть автомобиле с учетом комиссий и налогов

print("\t\t<<<Автодилер>>>".upper())

factory_car_price = int(input("\nВведите стоимость автомобиля в долларах: "))

print("\n====================================================")

print("\nСтоимость автомобиля до налогов и сборов:", factory_car_price)

print("\n====================================================")

print("\n\t\t<<<Налоги и сборы>>>".upper())

tax = int(factory_car_price / 100 * 5)
print("\nНалог на автомобиль 5%:", tax, "долларов")

registration_fee = int(factory_car_price / 100  * 3)
print("Регистрационный сбор 3%:", registration_fee, "долларов")

agency_fee = 250
print("Агентский сбор:", agency_fee, "долларов")

car_delivery = 500
print("Доставка автомобиля:", car_delivery, "долларов")

print("\n====================================================")

final_car_price = tax + registration_fee + agency_fee + car_delivery + factory_car_price
print("\nПолная стоимость автомобиля:", final_car_price, "долларов")

input("\n\nНажмите Enter, чтобы выйти")
