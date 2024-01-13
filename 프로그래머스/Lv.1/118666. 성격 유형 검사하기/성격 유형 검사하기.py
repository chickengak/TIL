def solution(survey, choices):
    answer = ''
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for sur, choice in zip(survey, choices):
        score = choice - 4
        if score < 0:
            scores[sur[0]] += abs(score)
        else:
            scores[sur[1]] += score
    if scores['R'] < scores['T']:
        answer += 'T'
    else:
        answer += 'R'
    if scores['C'] < scores['F']:
        answer += 'F'
    else:
        answer += 'C'
    if scores['J'] < scores['M']:
        answer += 'M'
    else:
        answer += 'J'
    if scores['A'] < scores['N']:
        answer += 'N'
    else:
        answer += 'A'
    return answer