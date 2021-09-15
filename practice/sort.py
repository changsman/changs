a=[1,10,2,6]
a.sort() ##오름차순 정렬 
print(a)
a.sort(reverse=True) ##내림차순 
print(a)

b=1423434   ###숫자를 문자열로 반환하여, 배열로 변환(str, list)
print(list(str(b))) ##해당 숫자를 배열로 변환
c= list(str(b))
print(c)

c.sort(reverse=True) #내림차순 하기(sort로 오름차순 정렬 후, reverse로 내림차순)
print(c)

d="".join(c) #join으로 배열합치기 
print(d)

#e=d(reverse=True)


def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

#####연습#####
number=(int(input('숫자를 입력하시오\n')))
print(solution(number))


