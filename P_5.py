import os


class Iterator1:
    def __init__(self, rating: str) -> None:
        """
        Конструктор класса. Инициализирует итератор для первого типа файлов.
        """
        self.file_names = os.listdir(
            os.path.join('data', rating))  # Получает список файлов в директории 'data' с указанным рейтингом.
        self.limit = len(self.file_names)
        self.counter = 0
        self.rating = rating

    def __next__(self) -> str:
        """
        Метод для получения следующего элемента в итераторе.
        """
        if self.counter < self.limit:  # Проверяет, не достиг ли счетчик предела.
            self.counter += 1
            return os.path.join(self.rating, self.file_names[self.counter - 1])  # Возвращает путь к следующему файлу.
        else:
            raise StopIteration

class Iterator2:
    def __init__(self, rating: str) -> None:
        """
        Конструктор класса. Инициализирует итератор для второго типа файлов.
        """
        if (5 < int(rating) or int(rating) < 1):
            raise KeyError
        self.file_names = []
        for name in os.listdir('data_copy'):
            if rating == name[0]:  # Проверяет, соответствует ли рейтинг начальной цифре имени файла.
                self.file_names.append(name)
        self.limit = len(self.file_names)
        self.counter = 0
        self.rating = rating

    def __next__(self) -> str:
        """
        Метод для получения следующего элемента в итераторе.
        """
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.file_names[self.counter - 1])
        else:
            raise StopIteration


a = Iterator1('1')

for i in range(10):  # Цикл проходит 10 раз.
    print(next(a))  # Выводит следующий элемент из итератора.
