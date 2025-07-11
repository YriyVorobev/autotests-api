#Работа с JSON в Python
import json
from itertools import filterfalse
from multiprocessing.resource_tracker import ensure_running

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)  # Преобразуем JSON-строку в Python-объект (dict)

print(parsed_data["name"])  # Выведет: Иван


data = {
    "name": "Мария",
    "age": 25,
    "is_student": True
}

json_string = json.dumps(data, indent=4 ,ensure_ascii = False)  # Преобразуем Python-объект в JSON-строку
print(json_string)

# with open("json_data.json", "r", encoding="utf-8") as file:
#     data = json.load(file)  # Загружаем JSON из файла
#     print(data)
#
# with open("json_data.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=4, ensure_ascii = False)  # Сохраняем JSON в файл