import json

json_data = '''{
  "name": "Ivan",
  "age": 36,
  "is_student": false,
  "courses": [
    "Python",
    "QA Automation",
    "API Testing"
  ],
  "address": {
    "city": "Donetsk", "zip": "101000"
  }
}'''

# Парсинг: преобразуем JSON-строку в Python-объект (dict)
parsed_data = json.loads(json_data)

print(parsed_data["name"])


#Обычный словарь в Python
data = {
    'name': 'Mariya',
    'age': 25,
    'is_student': True
}

# Сериализация: преобразуем Python-объект в JSON-строку
#indent используется для переноса строк (4 пробела)
json_string = json.dumps(data, indent=4)
print(json_string, type(json_string))

#открываем JSON файл на чтение
with open("json_example.json", "r", encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data, type(read_data))

#запись JSON в файл
with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)