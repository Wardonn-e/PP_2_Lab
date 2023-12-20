import os
import csv


def write(name_csv: str, rating: int) -> None:
    """
    Записывает пути к файлам и рейтинг в файл CSV.

    Args:
        name_csv (str): Имя файла CSV, в который будут записаны данные.
        rating (int): Рейтинг, соответствующий директории с файлами.

    Returns:
        None
    """
    full_path = os.path.abspath('data')
    name_review = os.listdir(os.path.join(full_path, str(rating)))  # Получает список файлов в директории, соответствующей заданному рейтингу.
    relative_path = os.path.relpath('data')
    with open(name_csv, 'a', newline='') as cs:
        for name in name_review:
            full_file_path = os.path.join(full_path, str(rating), name)
            relative_file_path = os.path.join(relative_path, str(rating), name)
            csv.writer(cs, delimiter=",", lineterminator='\r').writerow(
                [full_file_path, relative_file_path, rating])  # Записывает пути к файлам и рейтинг в файл CSV.


def create_csv_file(name_csv: str) -> None:
    """
    Создает файл CSV и записывает названия столбцов.

    Args:
        name_csv (str): Имя файла CSV.

    Returns:
        None
    """
    with open(name_csv, 'w') as csv_file:
        csv.writer(csv_file, delimiter=",", lineterminator='\r').writerow(
            ["absolute_path", "relative_path", "rating"])


def main() -> None:
    """
    Главная функция, создающая файл CSV и записывающая в него данные для каждого рейтинга.

    Returns:
        None
    """
    create_csv_file('1.csv')
    for i in range(1, 6):
        write('1.csv', i)  # Вызывает функцию write для каждого значения i.


if __name__ == "__main__":
    main()
