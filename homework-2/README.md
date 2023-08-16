# Режимы доступа. Домашнее задание

## Описание задачи

Внесите следующие изменения в класс `Item`:

- атрибут `name` сделать приватным
- добавить геттер и сеттер для `name`, используя @property
- в сеттере `name` проверять, что длина наименования товара не больше 10 симвовов.
- В противном случае, обрезать строку (оставить первые 10 символов).

Добавьте в `Item` следующие методы:
- `instantiate_from_csv()` - класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
- `string_to_number()` - статический метод, возвращающий число из числа-строки
> Для работы с csv-файлом используйте модуль `csv` и метод [`DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader)

Тестирование:
- Напишите тесты для новых методов в `tests/test_item.py`

## Ожидаемое поведение
- Код в файле `main.py` должен выдавать ожидаемые значения


''' def name(self, new_name):
        if not new_name.isalpha():
            raise ValueError("Имя должно состоять только из букв")
        self._name = new_name'''

'''with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])'
