import os
import shutil
import csv
import numpy
from P_2 import create
from P_2 import make_dir


def copy() -> None:
    """
    Копирование информации
    """
    random_integer_array = numpy.random.randint(0, 10000, 500)
    make_dir('data_copy3')
    k = 0
    for rating in os.listdir('data'):
        list_name = os.listdir(os.path.join('data', (rating)))
        for name in list_name:
            a = str(random_integer_array[k]).zfill(5)
            shutil.copy(os.path.join(os.path.join('data', rating), name),
                        os.path.join("data_copy3", a + '.txt'))
            with open('3.csv', 'a', newline='') as csv_file:
                csv.writer(csv_file, delimiter=",", lineterminator='\r').writerow(
                    [os.path.join(os.path.abspath('data_copy3'), a),
                     os.path.join(os.path.relpath('data_copy3'), a),
                     rating])
                k += 1


def main() -> None:
    create('3.csv')
    copy()


if __name__ == "__main__":
    main()
