import os
import shutil
import csv
import pandas as pd


def create(name_csv: str) -> None:
    """
    Эта функция создает файл CSV и записывает названия столбцов.
    """
    data = {
        "absolute_path": [],
        "relative_path": [],
        "rating": []
    }
    pd.DataFrame(data).to_csv(name_csv, index=False)


def make_dir(name: str) -> None:
    """
    Создание папки с указанным именем
    """
    if not os.path.isdir(name):
        os.mkdir(name)


def copy_info() -> None:
    """
    Копирование информации
    """
    make_dir('data_copy')
    for rating in os.listdir('data'):
        for name in os.listdir(os.path.join('data', (rating))):
            shutil.copyfile(os.path.join(os.path.join('data', rating), name),
                            os.path.join("data_copy", f"{rating}_{name}"))


def write(name_csv: str) -> None:
    """
    Функция записывает полный путь, относительный путь и рейтинг отзыва
    """
    with open(name_csv, 'a', newline='') as csv_file:
        for name in os.listdir('data_copy'):
            csv.writer(csv_file, delimiter=",", lineterminator='\r').writerow([os.path.join(os.path.abspath('data_copy')
            , name), os.path.join(os.path.relpath('data_copy'), name), name[0]])


def main() -> None:
    copy_info()
    create('2.csv')
    write('2.csv')


if __name__ == "__main__":
    main()
