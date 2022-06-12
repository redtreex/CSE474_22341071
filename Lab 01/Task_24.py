operator = input()
operand_1 = float(input())
operand_2 = float(input())


def calculate(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        return 'Invalid Number'


print(calculate(operator, operand_1, operand_2))