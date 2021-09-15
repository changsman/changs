def solution(x):
 answer=list(str(x))
 print(answer)

 for i in range(len(answer)):
    answer[i]=int(answer[i])
 print(answer)
 print(sum(answer))

 if x%sum(answer)==0:
   answer= True
 else:
   answer=False
 return answer
solution(10)


