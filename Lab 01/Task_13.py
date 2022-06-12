given_list = [21, 33, 44, 66, 11, 1, 88, 45, 10, 9]

def remove_odd(least):
    return [x for x in least if x % 2 == 0]

given_list = remove_odd(given_list)
print(given_list)
