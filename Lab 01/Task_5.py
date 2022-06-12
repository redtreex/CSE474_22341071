print('Enter value of S:')
S = int(input())
L = 69
if S < 100:
    L = 3000 - 125 * (S ** 2)
else:
    L = 12000 / 4 + (S ** 2) / 14900
print(L)
