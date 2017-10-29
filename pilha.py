def calculate(inputs):
    stack = []
    for a in inputs:
        if type(a) is int:
            stack.append(a)
            continue
        op1 = stack.pop()
        try:
            op2 = stack.pop()
        except:
            return op1
 
        if a == '+':
            stack.append(op2 + op1)
        elif a == '-':
            stack.append(op2 - op1)
        elif a == '*':
            stack.append(op2 * op1)
        elif a == '/':
            stack.append(op2 / op1)
 
    return stack.pop()
kek = []
while True:
    while '=' not in kek:
        o = input('Next:')
        try:
            kek.append(int(o))
        except:
            kek.append(o)
    print('Result: ' + str(calculate(kek)))
    kek.clear()

    

        
