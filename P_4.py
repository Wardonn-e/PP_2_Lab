import os


def get_next_element(rating: str) -> str:
    path = os.path.join("data", rating)  # Формирует путь к директории с заданным рейтингом.
    name_list = os.listdir(path)  # Получает список файлов в указанной директории.
    name_list.append(None)  # Добавляет значение None в конец списка.
    for i in range(len(name_list)):  # Цикл проходит по всем элементам списка.
        yield os.path.join(rating, name_list[i]) if name_list[i] is not None else None
        # Возвращает путь к файлу, если элемент не равен None, иначе возвращает None.


print(*get_next_element('1'))  # Выводит все элементы, возвращаемые генератором, через пробел.
