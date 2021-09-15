def solution(n):
    n=int(input())
    answer=""
    for i in range(n):
        if (i+1)%2==1:
         answer=answer+ "수"
        else:
         answer=answer+ "박" 
    
    return answer


print(solution(3))