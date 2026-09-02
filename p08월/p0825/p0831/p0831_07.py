# myNum=[]
# for i in range(6):
#     no=int(input("숫자입력: "))
#     if no not in myNum:
#         myNum.append(no)
#     else:print("중복된 번호 입니다.")
# print("입력한 수: ",myNum)

# i=0
# while i<6:
#         no=int(input("숫자입력: "))
#         if no not in myNum:
#             myNum.append(no)
#             i=i+1
#         else:print("중복된 번호 입니다.")
# print("입력한 수: ",myNum)



import random
# #한개의 랜덤문자
# a=random.randint(1,45)
# print(a)
# alist=list(range(1,46))
# random.shuffle(alist)
# print(alist)
# #랜덤으로 갯수만큼 추출(중복 없음)
# ranA=random.sample(range(1,46),6)
# print(ranA)
# #랜덤으로 개수만큼 추출(중복 가능)
# ranAA=random.choices()

lotto=random.sample(range(1,46),6)
print("로또 번호: ",lotto)

# 6개 입력부분
myNum = []  # 6개 입력
i = 0
while i<6:
    no = int(input("숫자입력 : "))
    if no not in myNum:
        myNum.append(no)
        i = i+1
    else:
        print("번호가 있습니다.")

# 정답확인 부분
answer = []
count = 0
for i in myNum:
    if i in lotto:
        count = count + 1
        answer.append(i)

print("로또번호: ",lotto)
print("내 번호: ",myNum)
print("맞춘 갯수: ",count)
print("맞춘 번호: ",answer)