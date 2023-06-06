import requests
import json

# Получение числа от пользователя
number = int(input("Введите число: "))

# Формирование URL на основе введенного числа
url = f"https://jsonplaceholder.typicode.com/todos/{number}"

# Загрузка данных из API
response = requests.get(url)
data = response.json()

# Запись данных в текстовый файл
filename = f"{data['id']}.json"
with open(filename, 'w') as file:
    json.dump(data, file)

print(f"Файл {filename} успешно создан.")
