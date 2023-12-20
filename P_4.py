import os


def get_next_element(rating: str) -> str:
    """
    Генератор, возвращающий пути к файлам в директории с заданным рейтингом.

    Args:
        rating (str): Рейтинг, для которого нужно получить пути к файлам.

    Yields:
        str: Путь к файлу в директории с заданным рейтингом или None, если файлов нет.
    """
    path = os.path.join("data", rating)  # Формирует путь к директории с заданным рейтингом.
    name_list = os.listdir(path)  # Получает список файлов в указанной директории.
    name_list.append(None)
    for i in range(len(name_list)):
        yield os.path.join(rating, name_list[i]) if name_list[i] is not None else None
        # Возвращает путь к файлу, если элемент не равен None, иначе возвращает None.


if __name__ == '__main__':
    print(*get_next_element('1'))
