def custom_map():
    my_nums = [1, 2, 3, 4, 5]
    for item in map(lambda num: num ** 2, my_nums):
        print(item)


def custom_filter():
    my_nums = [1, 2, 3, 4, 5, 6]
    return list(filter(lambda num: num % 2 == 0, my_nums))
