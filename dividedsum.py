def solution(n):
    answer = 0
    return answer

#a = input().split()
#print(a)
#a = list(map(int,input().split()))
#print(a)
##약수의 합##

num=10
array=[] 
count=0

for i in range(1,num+1):
    if(num%i==0):
       print(i)
       sum=i+num
       count=count+1

print(sum) 
print(array)

