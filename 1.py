import os
import csv

import os
import csv


def write(name_csv: str, rating: int) -> None:
    """
    Эта функция принимает имя файла CSV и рейтинг, затем записывает пути к файлам и рейтинг в файл CSV.
    """
    full_path = os.path.abspath('data')
    name_review = os.listdir(os.path.join(full_path, str(rating)))
    relative_path = os.path.relpath('data')
    with open(name_csv, 'a', newline='') as cs:
        for name in name_review:
            full_file_path = os.path.join(full_path, str(rating), name)
            relative_file_path = os.path.join(relative_path, str(rating), name)
            csv.writer(cs, delimiter=",", lineterminator='\r').writerow([full_file_path, relative_file_path, rating])


def create_csv_file(name_csv: str) -> None:
    """
    Эта функция создает файл CSV и записывает названия столбцов.
    """
    with open(name_csv, 'w') as csv_file:
        csv.writer(csv_file, delimiter=",", lineterminator='\r').writerow(["absolute_path", "relative_path", "rating"])


def main() -> None:
    create_csv_file('1.csv')
    for i in range(1, 6):
        write('1.csv', i)


if __name__ == "__main__":
    main()
