def evalRPN(tokens):
    stack = []

    for token in tokens:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            num1, num2 = stack.pop(), stack.pop()
            stack.append(num2 - num1)
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            num1, num2 = stack.pop(), stack.pop()
            stack.append(int(num2 / num1))
        else:
            stack.append(int(token))

    return stack[0]


print(evalRPN(["2", "1", "+", "3", "*"]))
