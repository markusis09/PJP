
def compute_expression(expression): # 1+2*3+4
    return eval(expression)

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


rows_count = 1
for i in range(rows_count):
    expression = '1+(2*(3+4)+5)'
    expression = expression.replace(' ', '')
    expression = remove_brackets(expression)
    print(expression)
