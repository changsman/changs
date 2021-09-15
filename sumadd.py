def solution(n):
    array=list(str(n))
    for i in range(len(array)):
     array[i]=int(array[i])
    answer=sum(array)    

    return answer

print(solution(1233))



a=674
array=list(str(a))
print(array)
print(type(array[0]))

for i in range(len(array)):
 array[i]=int(array[i])

print(type(array))
print(sum(array))



#cnt=len(array)
#print(type(cnt))

#for i in range(cnt) :
#    answer=int(a/10**(cnt-1-i))
#    print(answer)