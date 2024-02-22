def solution(expression):
    expressions = []
    temp = ''
    for c in expression:
        if c.isdigit():
            temp += c
        else:
            expressions.append(temp)
            expressions.append(c)
            temp = ''
    expressions.append(temp)

    answers = []
    operators = ['+-*', '+*-', '-+*', '-*+', '*+-', '*-+']
    for op_list in operators:
        res = expressions[:]

        for op in op_list:
            temp = []
            skip = False
            for i in range(0, len(res)):
                if skip:
                    skip = False
                    continue
                if res[i] == op:
                    temp.append(str(eval(temp.pop() + res[i] + res[i+1])))
                    skip = True
                else:
                    temp.append(res[i])
            res = temp
        answers.append(abs(int(res[0])))

    return max(answers)