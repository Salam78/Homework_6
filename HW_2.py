def access_array_element(array, index):
    try:
        element = array[index]
        print(f"Значение элемента с индексом {index}: {element}")
    except IndexError:
        print("Ошибка: индекс выходит за границы массива!")

my_array = [1, 2, 3, 4, 5]

index = int(input("Введите индекс элемента: "))

access_array_element(my_array, index)
input("press any key to close window")
