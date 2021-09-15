def solution(nums):
    nums_array=list(set(nums))
    if len(nums_array)>len(nums)//2:
            
      answer = len(nums)//2
      return answer
    else:
     answer=len(nums_array)
     return answer
