from secrets import compare_digest


def infix_to_npi(expression):
    stack = []
    output = []

    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in operators:
            while stack and stack[-1] in operators and operators[token] <= operators[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
        elif compare_digest(token, '('):
            stack.append(token)
        elif compare_digest(token, ')'):
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return ' '.join(output)


def evaluate_npi(npi_expression):
    stack = []

    for token in npi_expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if compare_digest(token, '+'):
                stack.append(op1 + op2)
            elif compare_digest(token, '-'):
                stack.append(op1 - op2)
            elif compare_digest(token, '*'):
                stack.append(op1 * op2)
            elif compare_digest(token, '/'):
                stack.append(op1 / op2)
            elif compare_digest(token, '^'):
                stack.append(op1 ** op2)

    return stack[0]


def validate_transformation(string_value):
    new_formula = ''
    table = list(string_value)
    return_value = 0
    nb_value = 0
    for i in range(len(table)):
        if table[i] == '(':
            return_value = 1
            nb_value += 1
            continue
        if table[i] == ')':
            return_value = 0
            nb_value -= 1
            continue
        else:
            new_formula = new_formula + table[i] + ''
    if return_value == 1 or nb_value != 0:
        raise 'expression error'
    return return_value, new_formula


if __name__ == '__main__':
    expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 "
    fu = validate_transformation(expression)
    print(expression)
    npi_expression = infix_to_npi(expression)
    print(npi_expression)
    res = evaluate_npi(npi_expression)
    print(res)
