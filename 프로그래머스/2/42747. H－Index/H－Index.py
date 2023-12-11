def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i+1:
            return max(citations[i], i)
    else:
        return len(citations)
    # citations.sort()
    # for i in range(len(citations)-1, -1, -1):
    #     if len(citations)-i >= citations[i]:
    #         return citations[i]
    # else:
    #     return len(citations)