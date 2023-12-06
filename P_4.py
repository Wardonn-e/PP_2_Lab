import os


def get_next_element(rating: str) -> str:
    path = os.path.join("data", rating)
    name_list = os.listdir(path)
    name_list.append(None)
    for i in range(len(name_list)):
        yield os.path.join(rating, name_list[i]) if name_list[i] is not None else None


print(*get_next_element('1'))