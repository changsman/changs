
def solution(n):
   list_n=list(str(n))
   for i in range(len(list_n)):
    list_n[i]=int(list_n[i])
   list_n.sort()
   list_n.reverse()
   len(list_n)
   sum=0
   
   for i in range(len(list_n)):
    sum=sum+list_n[i]*10**(len(list_n)-1-i)

   return sum

print(solution(43435300))



a=342
list_a=list(str(a))

for i in range(len(list_a)):
    list_a[i]=int(list_a[i])
list_a.sort()
list_a.reverse()
len(list_a)
sum=0
for i in range(len(list_a)):
    sum=sum+list_a[i]*10**(len(list_a)-1-i)




