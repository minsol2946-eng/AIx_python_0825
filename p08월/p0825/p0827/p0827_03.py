#입력한 숫자가 양수 인지, 음수 인지 출력.
#1.숫자입력 2. 양수 3. 음수 비교 3. 출력

# a=int(input("숫자입력: "))
# if a>0:
#     print("양수 입니다.")
# else:
#     print("음수 입니다.")
# print("입력 숫자: " ,a)

#------------------------------------------
#입력한 숫자가 2의 배수인지, 아닌지 출력.

# a=int(input("숫자를 입력하세요."))
# if a%2==0:
#     print("2의 배수 입니다.")
# else:
#     print("2의 배수가 아닙니다")
# print("입력한 숫자: ", a)

#--------------------------------------------
# #랜덤함수 import random -파이썬에 있는 random 클래스를 사용하겠다고 선언.
# import random
# #1~100까지 랜덤으로 정수값을 1개 넘겨줌
# num=random.randint(1,100)
# print(num)

#1~5 랜덤 숫자를 출력하시오.
# num=random.randint(1,5)
# input1=int(input("1~5 범위의 숫자를 입력하세요. "))
# print("랜덤숫자: ",num)
# print("랜덤숫자: " ,input1)
# if num==input1:
#     print("당첨!!")
# else:
#     print("꽝!!")

import random

num=random.randint(1,10)
a=int(input("1-10 범위의 숫자를 입력하세요."))
b=int(input("1-10 범위의 숫자를 입력하세요."))

print("랜덤숫자: " ,num)
print("입력숫자: " ,a)
print("입력숫자: " ,b)

if (num==a) or (num==b):
    print("당첨!")
else:
    print("꽝")