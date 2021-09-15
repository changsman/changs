def solution(a, b):
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    day=['THU','FRI','SAT','SUN','MON','TUE','WED']
    sum=0
    for i in range(a-1):
      sum=sum+month[i]
    
    sum=b+sum
    date=sum%7
    
    answer=day[date]
      
    return answer

print(solution(1,8))