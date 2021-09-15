#x,n=map(int,input().split())
#sum=0

#for i in range(n):
#  sum=sum+(i+1)*x
#print(sum)

def solution(x, n):
    sum=[]
    for i in range(n):
        sum.append((i+1)*x)
    return sum    
  

print(solution(2,5))

