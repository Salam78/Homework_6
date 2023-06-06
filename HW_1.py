def plus_two(number):
    try:
        result = 2 + number
        print(f"Результат: {result}")
    except TypeError:
        print("Ожидаемый тип данных - число!")

number = input("Введите число: ")

try:
    number = int(number)
    plus_two(number)
except ValueError:
    print("Ожидаемый тип данных - число!")
input("press any key to close window")
