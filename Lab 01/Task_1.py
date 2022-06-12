print('Enter a number:')
user_input_1 = int(input())
print('Enter another number:')
user_input_2 = int(input())

print("Sum of the two numbers:", str(user_input_1 + user_input_2))
print("Product of the two numbers:", str(user_input_1 * user_input_2))
print("Difference between the two numbers:", abs(user_input_1-user_input_2))

if user_input_1 > user_input_2:
    print('First is greater')
else:
    print('Second is greater')