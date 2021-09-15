def solution(arr):
 
 if len(arr)==1:
  return -1
 
 else:
  for i in arr:
   min_num=min(arr)
  arr.remove(min_num)
 return arr


print(solution([10,20]))



arr_list=[5,2,3]
for i in arr_list:
  min_num=min(arr_list)
    
arr_list.remove(min_num)
print(arr_list)