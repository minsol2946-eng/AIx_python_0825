# for i in range(1,11):
#     print(i)
# print("-"*50)
# i=1
# while(i<11):    #조건식이 True때만.
#     print(i)
#     i+=1


# #모든 for 문은 while문 변경 가능.
# #for:반복, 구간지정 1-10
# #while: 조건식이 있을때, 주로 사용, 무한반복 일 때 사용.

# i=0
# while True:
#     print(i)
#     i+=1


# alist=list(range(10))
# #while문은 사용해서 alist에 있는 값을 출력.
# i=0
# while(i<10):
#     print(i,end="")
#     i+=1

# alist=["바나나","딸기","수박"]
# i=0
# while i<3:
#     print(f"{i}.{alist[i]}")
#     i+=1    #증감식 필수
# for i in alist:
#     print(f"{i},{alist[i]}")

# i=0
# while True:
#     print(i)
#     if i%10==0:
#         input1=input("프로그램을 종료할까요?")
#         if input1=="x":
#             break
#     i+=1

# print("프로그램 종료")

# # 두 수를 입력 받아 합을 구하는 무한반복 프로그램을 구현.
# while True:
#     a=int(input("1.숫자 입력: "))
#     if a==0:break
#     b=int(input("2.숫자 입력: "))
#     if b==0:break
#     print("합: ",a+b)

# print("종료")
