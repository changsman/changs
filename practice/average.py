def solution(arr):
    if(arr==0):
        return 0
    
    answer= sum(arr) /len(arr)
    return answer


number=[1,2,3]
print("평균값은",solution(number))