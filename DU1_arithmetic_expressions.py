
def operation(a, b, operator):
    if operator == '*':
        return a * b
    elif operator == '/':
        return a // b
    elif operator == '+':
        return a + b
    elif operator == '-':
        return a - b

def build_new_expression(expression, i):
    j = i
    k = i
    while j-1 > 0 and expression[j-1].isdigit():
        j -= 1
    while k+1 < len(expression) and expression[k+1].isdigit():
        k += 1

    if(j > 1):
        return expression[:j] + str(operation(int(expression[j:i]), int(expression[i+1:k+1]), expression[i])) + expression[k+1:]
    return expression[:j-1] + str(operation(int(expression[j-1:i]), int(expression[i+1:k+1]), expression[i])) + expression[k+1:]


def compute_expression(expression): # 1+2*3+4
    i = 0
    while i < len(expression):
        if(expression[i] == '*' or expression[i] == '/'):
            expression = compute_expression(build_new_expression(expression, i))
            break
        i+=1
    i = 0
    while i < len(expression):
        if(expression[i] == '+' or expression[i] == '-'):
            expression = compute_expression(build_new_expression(expression, i))
            break
        i+=1
    return expression


def remove_brackets(expression): # 1*(3+5) / 2 + 1 * 4 + ((4+5) * 2) +1
    i = 0
    while i < len(expression):
        if expression[i] == ')':
            for j in range(i, -1, -1):
                if expression[j] == '(':
                    expression = remove_brackets(expression[:j] + str(compute_expression(expression[j+1:i])) + expression[i+1:])
                    break
            break
        i+=1
    return expression


rows_count = int(input())
solved_expressions = []

for i in range(rows_count):
    expression = input()
    try:
        expression = expression.replace(' ', '')
        expression = remove_brackets(expression)
        expression = compute_expression(expression)
    except:
        expression = 'ERROR'
    solved_expressions.append(expression)

for expression in solved_expressions:
    print(expression)
