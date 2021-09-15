def solution(numbers):
    answer = []
    result=[]
    for i in range(len(numbers)):
     for j in range(i+1,len(numbers)):
      answer.append(numbers[i]+numbers[j])
    for i in answer:
     if i not in result:
      result.append(i)
    result.sort()
    return result