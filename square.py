def solution(n):
 for i in range(1,n+1):
  if n%i==0:
     if n==i**2:             
        answer=(i+1)**2
        return answer
 else:
    return -1 

print(solution(36))                
#    cnt=len(arr)
#    
#    if cnt%2==1:
#         index=int((cnt-1)/2)
#        number=arr[index]+1 
#         answer = number**2
#        return answer 
#    else: 
#         return -1
   



#arr=[]
#for i in range(1,26):
#    if 25%i==0:
#        arr.append(i)
#        
#cnt=len(arr)
#print(cnt,type(cnt))
#print(arr[1])

#if cnt%2==1:
#    index=int((cnt-1)/2)
#    print(index)
#    print("제곱근은",arr[index], "입니다")
#    n=arr[index]+1
#    print(n**2)

#else:
#   print("제곱근은 없습니다") 



