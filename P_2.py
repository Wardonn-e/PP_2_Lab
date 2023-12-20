import os
import shutil
import csv
from pathlib import Path
import pandas as pd


def create(name_csv: str) -> None:
    """
    Создает файл CSV и записывает названия столбцов.

    Args:
        name_csv (str): Имя файла CSV.

    Returns:
        None
    """
    data = {
        "absolute_path": [],
        "relative_path": [],
        "rating": []
    }
    pd.DataFrame(data).to_csv(name_csv, index=False)


def make_dir(name: str) -> None:
    """
    Создает папку с указанным именем.

    Args:
        name (str): Имя папки.

    Returns:
        None
    """
    path = Path(name)
    if not path.is_dir():
        path.mkdir()


def copy_info() -> None:
    """
    Копирует информацию из одной директории в другую.

    Returns:
        None
    """
    make_dir('data_copy')
    source_dir = Path('data')
    for rating_dir in source_dir.iterdir():
        if rating_dir.is_dir():
            for file_path in rating_dir.iterdir():
                if file_path.is_file():
                    destination_path = os.path.join("data_copy", f"{rating_dir.name}_{file_path.name}")
                    shutil.copyfile(file_path, destination_path)


def write(name_csv: str) -> None:
    """
    Записывает полный путь, относительный путь и рейтинг отзыва в файл CSV.

    Args:
        name_csv (str): Имя файла CSV.

    Returns:
        None
    """
    with open(name_csv, 'a', newline='') as csv_file:
        for file_path in Path('data_copy').iterdir():
            if file_path.is_file():
                absolute_path = file_path.resolve()
                relative_path = file_path.relative_to('data_copy')
                rating = file_path.name[0]
                csv.writer(csv_file, delimiter=",", lineterminator='\r').writerow(
                    [str(absolute_path), str(relative_path), rating])


def main() -> None:
    """
    Основная функция, копирующая информацию и создающая CSV файл.

    Returns:
        None
    """
    try:
        copy_info()
        create('2.csv')
        write('2.csv')
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
