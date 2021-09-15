def solution(absolutes, signs):
    res = []
    for idx in range(len(signs)):
        if signs[idx] == True:
            res.append(absolutes[idx])
        else:
            res.append(-absolutes[idx])
    return sum(res)

print(solution([4,7,12], [True,False,True]))
 
print(solution([4,1],["true","false"]))