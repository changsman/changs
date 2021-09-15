def solution(arr, divisor):
 answer=[]
 answer=[num for num in arr if num % divisor == 0]
 if len(answer)>0:
  answer.sort()
  return answer
 else:
  answer=[-1]
  return -1
print(solution([3,25,5,1,34],5))
#
#
#
#
arr=[3,25,5,1,34]
divisor=5
answer = [num for num in arr if num % divisor == 0]
answer.sort()
print(answer)