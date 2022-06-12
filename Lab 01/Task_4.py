print('Enter hours worked:')
hours = int(input())

if hours <= 40:
    print(hours * 200)
else:
    print(8000 + ((hours - 40) * 300))
