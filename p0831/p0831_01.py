# # 이름입력을 3번 반복하시오.
# name = []
# for i in range(3):
#     a = input("이름입력 : ")
#     name.append(a)  # 리스트:append,insert,extend

# print("[ 학생명단 ]")
# print(name)
# for n in name:
#     print(n)
# # [ 학생명단 ]
# # 홍길동
# # 유관순
# # 이순신


# for i in range(3): # 0,1,2
#     print(i)

# for i in range(1,6):
#     print(i)
# print("-"*10)
# for i in range(1,11,2):
#     print(i)

# for i in range(1,11):
#     print(i)

# #1,2,3,---10->2-,30,40
# for i in range(1,11):
#     print(i*10)

# arrs=[1,3,5,7]
# for arr in arrs:
#     print(arr)

# fruit=["사과","배","바나나"]
# for f in fruit:
#     print(f)

# #입력한 숫자가 홀수인지, 짝수인지 구분 출력.
# a=int(input("숫자 입력: "))
# if a%2==0:print("짝수입니다.")
# else:print("홀수입니다.")

nums=[3,9,10,105,220,2,1]
for n in nums:
    # print(n)
    if n%2==0:print(n,":짝수 입니다.")
    else:pass #print(n,":홀수 입니다.")

#반복문
# for i in range(10)/range(1,11)/range(1,11,2)/[1,2,3]/"안녕하세요"

# 구구단출력
# for i in range(2,10):
#     print(i,"X",1,"=",i*1)
#     print("{} X {} = {}".format(i,1,i*1))
#     print(f"{i} x {1} = {i*1}")

# for i in range(2,10):
#     print(" [ {}단 ]".format(i))
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j),end="  ")
#     print()

for i in range(2,10):
    for j in range(1,10):
        print("{}x{}={}".format(i,j,i*j),end="\t")
    print()