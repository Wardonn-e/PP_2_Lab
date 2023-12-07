import os


class Iterator1:
    def __init__(self, rating: str) -> None:
        self.file_names = os.listdir(os.path.join('data', rating))
        self.limit = len(self.file_names)
        self.counter = 0
        self.rating = rating

    def __next__(self) -> str:
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.rating, self.file_names[self.counter - 1])
        else:
            raise StopIteration


class Iterator2:
    def __init__(self, rating: str) -> None:
        if (5 < int(rating) or int(rating) < 1):
            raise KeyError
        self.file_names = []
        for name in os.listdir('data_copy'):
            if rating == name[0]:
                self.file_names.append(name)

        self.limit = len(self.file_names)
        self.counter = 0
        self.rating = rating

    def __next__(self) -> str:
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.file_names[self.counter - 1])
        else:
            raise StopIteration


a = Iterator1('1')
for i in range(10):
    print(next(a))
