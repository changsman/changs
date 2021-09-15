def solution(s):
    answer = ''
    if len(s)%2==1:
      answer=answer+s[(len(s)-1)//2]  
      return answer
    else:
     answer=s[(len(s)-1)//2]+s[(len(s)-1)//2+1]
     return answer
