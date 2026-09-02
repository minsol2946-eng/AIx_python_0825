# #함수는 호출하는 명렁어 위에 있어야 한다.
# #함수의 매개 변수 갯수가 다르면 error

# def print1(num1,str1):
#     for i in range(num1):
#         print(i+1,str1)


# while True:
#     num1=int(input("숫자입력: "))
#     str1=input("출력 문구 입력: ")
#     print1(num1,str1)


# #함수 리턴
# def add(num1,num2):
#     sum=num1+num2
#     return sum      #호출 하는 곳으로 값 전달

# while True:
#     num1=int(input("숫자입력: "))
#     num2=int(input("숫자입력: "))
#     total=add(num1,num2)
#     print("결과값: ",total)


def cal(num1,num2,str1):
    result=0
    if str1=="+":
        reasult=num1+num2
    elif str1=="-":
        result=num1-num2
    elif str1=="*":
        result=num1*num2
    elif str1=="/":
        result=num1/num2
    return result

num1=int(input("숫자입력: "))
num2=int(input("숫자입력: "))
str1=input("+,-,*/ 중 1개 입력: ")
result=cal(num1,num2,str1)
print(f"결과값:{num1}{str1}{num2}={result}")