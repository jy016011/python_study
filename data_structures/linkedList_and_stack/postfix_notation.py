from stack import LinkedListStack

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution1(S):
    global prec
    opStack = LinkedListStack()
    answer = ''
    for ch in S:
        if ch == '(':
            opStack.push(ch)
        elif ch == ')':
            while not opStack.isEmpty() and opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
        elif ch in prec.keys():
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[ch]:
                answer += opStack.pop()
            opStack.push(ch)
        elif ch not in prec.keys():
            answer += ch
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer


print(solution1("(A+B)*(C+D)") == "AB+CD+*")
print(solution1("A*B+C") == "AB*C+")
print(solution1("A+B*C") == "ABC*+")
print(solution1("A+B+C") == "AB+C+")
print(solution1("(A+B)*C") == "AB+C*")
print(solution1("A*(B+C)") == "ABC+*")

def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens

def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = LinkedListStack()
    postfixList = []

    for token in tokenList:
        if token == '(':
            opStack.push(token)
        elif token == ')':
            while not opStack.isEmpty() and opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        elif token in prec.keys():
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)
        else:
            postfixList.append(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    op = ['*', '/', '+', '-']
    number_stack = LinkedListStack()
    for token in tokenList:
        if token not in op:
            number_stack.push(token)
        else:
            numbers = [number_stack.pop() for _ in range(2) if not number_stack.isEmpty()]
            if len(numbers) == 2:
                op_result = eval(str(numbers[1]) + token + str(numbers[0]))
                number_stack.push(op_result)

    return number_stack.pop()


def solution2(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

print(solution2("5 + 3") == 8)
print(solution2("(1 + 2) * (3 + 4)") == 21)
print(solution2("7 * (9 - (3 + 2))") == 28)