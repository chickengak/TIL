def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))
    answers = [ sum([data[r][c]%(r+1) for c in range(len(data[0]))]) for r in range(row_begin-1, row_end)]
    res = 0
    for ans in answers:
        res = res ^ ans
    return res