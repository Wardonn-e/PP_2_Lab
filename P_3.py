import os
import shutil
import csv
import numpy
from P_2 import create
from P_2 import make_dir

def copy() -> None:
    """
    Копирует информацию.

    Использует случайно сгенерированные целочисленные значения для создания новых файлов с разными именами,
    копирует их в новую директорию 'data_copy3' и записывает пути к файлам в файл CSV '3.csv'.

    Returns:
        None
    """
    random_integer_array = numpy.random.randint(0, 10000, 500)
    make_dir('data_copy3')
    k = 0
    for rating in os.listdir('data'):
        rating_path = os.path.join('data', rating)
        if os.path.isdir(rating_path):  # Проверяет, является ли это директорией
            list_name = os.listdir(rating_path)
            for name in list_name:
                a = str(random_integer_array[k]).zfill(5)
                file_path_source = os.path.join(rating_path, name)
                file_path_destination = os.path.join("data_copy3", a + '.txt')
                shutil.copy(file_path_source, file_path_destination)
                with open('3.csv', 'a', newline='') as csv_file:
                    csv.writer(csv_file, delimiter=",", lineterminator='\r').writerow(
                        [os.path.abspath(file_path_destination),
                         os.path.relpath(file_path_destination),
                         rating])
                    k += 1

def main() -> None:
    """
    Основная функция, создающая файл CSV '3.csv' и копирующая информацию.

    Returns:
        None
    """
    create('3.csv')
    copy()

if __name__ == "__main__":
    main()
