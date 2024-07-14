import random


def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result


def average(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)


def round_list(list_of_numbers):
    return [round(num) for num in list_of_numbers]


if __name__ == '__main__':
    # список из 10 целых случайных чисел от -10 до 10
    list1 = [random.randint(-10, 10) for _ in range(10)]
    # список из 10 вещественных случайных чисел от -10 до 10
    list2 = [random.random() * 20 - 10 for _ in range(10)]
    # список из 10 смешанных (целых и вещественных) случайных чисел от -10 до 10
    list3 = [random.randint(-10, 10) if random.randint(0, 1) else random.random() * 20 - 10 for _ in range(10)]

    print(apply_all_func(list1, min, max))
    print(apply_all_func(list2, len, sum, sorted))
    print(apply_all_func(list3, min, max, sum, sorted))
    print(apply_all_func(list1, sum, average))
    print(apply_all_func(list3, max, min, round_list))
