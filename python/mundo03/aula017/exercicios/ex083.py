# Validating mathematical expressions
# Create a program where the user enters any expression that uses parentheses.
# Your application should analyse if the expression informed has the open and closed parentheses at the right order.
expression = str(input('Enter an expression: '))
print(expression)
expression = expression.replace(' ', '')
expression_list = []
for _c in expression:
    expression_list.append(_c)
parentheses = []
for _c in expression_list:
    if _c == '(' or _c == ')':
        parentheses.append(_c)
if len(parentheses) != 0:
    if parentheses[0] == '(' and len(parentheses) > 1:
        open_parentheses = 0
        closed_parentheses = 0
        while True:
            if parentheses[0] == '(':
                parentheses.pop(0)
                open_parentheses += 1
            elif parentheses[0] == ')':
                parentheses.pop(0)
                closed_parentheses += 1
            if len(parentheses) == 1 and parentheses[0] == '(':
                print('This is not a valid expression')
                break
            if len(parentheses) == 0:
                if open_parentheses == closed_parentheses:
                    print('This is a valid expression')
                else:
                    print('This is not a valid expression')
                break
    else:
        print('This is not a valid expression')
else:
    print('This is a valid expression, and has no parentheses')

# Teacher's solution
expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
