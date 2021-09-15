def solution(number, k):
 answer=''
 result=''
 arr=str(number)
 for i in arr:
  answer.append(''.join(i))    
 answer.sort(reverse=True)
 ###['5','4','3','2']
 for i in answer[0:k]:
  result=answer[i]+answer
 return answer

print(solution(1234,2))