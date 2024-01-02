def solution(numbers, hand):
    answer = ''
    left = (0,0)
    right = (2,0)
    buttons = {1:(0,3), 2:(1,3), 3:(2,3), 4:(0,2), 5:(1,2), 6:(2,2), 7:(0,1),8:(1,1),9:(2,1), 0:(1,0)}
    for number in numbers:
        if number in (1, 4, 7):
            answer += 'L'
            left = buttons[number]
        elif number in (3,6,9):
            answer += 'R'
            right = buttons[number]
        else:
            left_distance = abs(left[0]-buttons[number][0]) + abs(left[1]-buttons[number][1])
            right_distance = abs(right[0]-buttons[number][0]) + abs(right[1]-buttons[number][1])
            if left_distance < right_distance:
                answer += 'L'
                left = buttons[number]
            elif left_distance > right_distance:
                answer += 'R'
                right = buttons[number]
            else:
                if hand == "left":
                    answer += 'L'
                    left = buttons[number]
                else:
                    answer += 'R'
                    right = buttons[number]
                
    return answer