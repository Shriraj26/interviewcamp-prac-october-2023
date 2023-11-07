"""
Infix with Brackets - 
0. ( and ) will 0 priority
1. When (, add to operator stack
2. when ), process till top of operator is not (
3. Then pop
"""

def infixWithoutBrackets(arr):

    pref = {'+': 1, '-' : 1, '/' : 2, '*' : 2}
    operandStack = []
    operatorStack = []

    for elem in arr:
        if elem in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # push in operand stack
            operandStack.append(int(elem))
        else:

            while len(operatorStack) and pref[elem] <= pref[operatorStack[-1]]:
                process(operandStack, operatorStack)
            operatorStack.append(elem)
    

    while len(operatorStack):
        process(operandStack, operatorStack)
    
    return operandStack[-1]

def process(operandStack, operatorStack):
    print(operandStack, operatorStack)
    # pop 2 elems from operand stack
    elem2 = operandStack.pop()
    elem1 = operandStack.pop()
    operator = operatorStack.pop()

    result = 0

    if operator == '+':
        result = elem1 + elem2
    elif operator == '-':
        result = elem1 - elem2
    elif operator == '/':
        result = elem1 / elem2
    elif operator == '*':
        result = elem1 * elem2

    operandStack.append(result)
    


arr = '1+2/1+3*2'
# print(infixWithoutBrackets(arr))


def infixWithBrackets(arr):

    pref = {'+': 1, '-' : 1, '/' : 2, '*' : 2, '(': 0, ')': 0}
    operandStack = []
    operatorStack = []

    for elem in arr:
        if elem in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # push in operand stack
            operandStack.append(int(elem))
        else:

            if elem == '(':
                operatorStack.append(elem)
            elif elem == ')':
                while operatorStack[-1] != '(':
                    process(operandStack, operatorStack)
                operatorStack.pop()
            else:
                while len(operatorStack) and pref[elem] <= pref[operatorStack[-1]]:
                    process(operandStack, operatorStack)
                operatorStack.append(elem)


    while len(operatorStack):
        process(operandStack, operatorStack)
    
    return operandStack[-1]

print(infixWithBrackets('1+2/(1+3)*2'))