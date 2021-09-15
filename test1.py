n=int(input())
answer=''
while n>0:
 n,mod=divmod(n,3)
 answer=str(mod)+answer
print(n)
print(answer)
print(type(answer))
answer.reverse()
answer=int(answer)
print(type(answer))
print(answer)

def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums.sort()
    last = 0
    
    for i in nums :
        if i not in nums:
            answer +=1
            last = value
            
    return answer