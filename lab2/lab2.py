def calc(data):
    def operation(op, x, y):
        operators = {
            '+': x + y,
            '-': x - y,
            '*': x * y,
            '/': x / y
        }
        return operators[op]

    operators = '+-*/'

    operator = ''
    for i in range(1, len(data)):
        if data[i] in operators:
            operator = data[i]
            break

    parts = data.split(operator, 1)
    return operation(operator, int(parts[0]), int(parts[1]))


print(calc('9/3'))
print(calc('8    + 3'))
data = input('---')
print(calc(data))