def solution(genres, plays):
    dic = {}
    for i, p in enumerate(plays):
        try:
            dic[genres[i]]["sum"] += p
            if p > dic[genres[i]]["fir"][1]:
                dic[genres[i]]["sec"] = dic[genres[i]]["fir"]
                dic[genres[i]]["fir"] = [i, p]
            elif p > dic[genres[i]]["sec"][1]:
                dic[genres[i]]["sec"] = [i, p]
        except:
            dic[genres[i]] = {"sum": p, "sec": [-1,-1] , "fir":[i,p]}
    result = sorted(dic.values(), key=lambda x: x["sum"], reverse=True)
    ans = []
    for res in result:
        ans.append(res["fir"][0])
        if res["sec"][0] != -1:
            ans.append(res["sec"][0])
    return ans