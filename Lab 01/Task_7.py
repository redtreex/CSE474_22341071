print('Enter value of n:')
n = int(input())
sum_even = 0
sum_odd = 0
for i in range(1, n+1, 2):
    sum_odd = sum_odd + i**2
for i in range(0, n+1, 2):
    sum_even = sum_even - i**2

print(sum_odd+sum_even)
