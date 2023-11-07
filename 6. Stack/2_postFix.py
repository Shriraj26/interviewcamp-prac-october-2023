"""
    1 5 + 2 -  -->  1 + 5 - 2
"""

def postFix(arr):

    operandStack = []

    for elem in arr:
        if elem in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # push in operand stack
            operandStack.append(int(elem))

        else:
            # process
            process(operandStack, elem)
    
    return operandStack[-1]

def process(operandStack, operator):

    # pop 2 elems from operand stack
    elem2 = operandStack.pop()
    elem1 = operandStack.pop()
    
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

arr = '15+2-'
print(postFix(arr))
