# b) -10, -5, 0, 5, 10, 15, 20
print('b)', end='')
for i in range(-10, 21, 5):
    if i != 20:
        print(i, end=', ')
    else:
        print(i, end='')

# c) 18, 27, 36, 45, 54, 63
print('\nc)', end='')
for i in range(2, 8):
    if i != 7:
        print(i * 9, end=', ')
    else:
        print(i * 9, end='')

# d) 18,-27, 36,-45,54,-63
print('\nd)', end='')
for i in range(2, 8):
    if i % 2 != 0:
        i = i * (-1)
    if i != 7:
        print(i * 9, end=', ')
    else:
        print(i * 9, end='')
