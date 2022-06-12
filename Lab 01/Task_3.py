print("Enter student's mark:")
mark = int(input())

if mark < 50:
    print('F')
elif mark < 60:
    print('E')
elif mark < 70:
    print('D')
elif mark < 80:
    print('C')
elif mark < 90:
    print('B')
elif mark <= 100:
    print('A')
else:
    print('Invalid Input')