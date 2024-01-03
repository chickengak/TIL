def solution(order):
    stack = []
    order_idx = 0
    box_number = 1
    while order_idx != len(order):
        if order[order_idx] == box_number:
            order_idx +=1
            box_number +=1
        elif stack and order[order_idx] == stack[-1]:
            stack.pop()
            order_idx +=1
        elif order[order_idx] < box_number:
            return order_idx
        else:
            stack.append(box_number)
            box_number +=1
    return order_idx