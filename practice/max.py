count=int(input("수열의 개수를 입력하세요"))
array=[]
for i in range(count):
    array.append(int(input().split()))

array.sort()
for i in array:
    print(i, end=' ')


print(array)

    