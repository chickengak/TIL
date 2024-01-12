def solution(sequence, k):
    answer = []
    cur_length = 1_000_000
    from_idx = len(sequence)
    to_idx = len(sequence) -1
    total = 0
    while from_idx >= 0:
        if total == k:
            if (to_idx - from_idx) <= cur_length:
                cur_length = to_idx - from_idx
                answer = [from_idx, to_idx]
            else:
                break

        if total <= k:
            from_idx -= 1
            total += sequence[from_idx]
        else:
            total -= sequence[to_idx]
            to_idx -= 1

    return answer