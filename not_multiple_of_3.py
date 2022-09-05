def not_multiple_of_3(func):
    list_1 = []

    def wrapper(*args):
        nonlocal list_1
        f1 = func(*args)
        list_1 = [x for x in f1 if x % 3 != 0]
        print(f'Количество чисел не кратных 3 = {len(list_1)}.')
        return f1

    return wrapper


@not_multiple_of_3
def multiple_of_3(*args):
    list_ = [x for el in args for x in el]
    list_3 = [x for x in list_ if x % 3 == 0]
    print(list_3)

    return list_


multiple_of_3([1, 2, 3], [4, 5, 6], [7, 8, 9])
