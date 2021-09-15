def hide_numbers(s):
  return '*' * (len(s) - 4) + s[-4:]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));
a='01033334444'
print(len(a))
print(a[0])


num=input()
print(type(num))
cnt=len(num)
num='*'* (len(num)-4) + num[:cnt-1] 
print(num)

