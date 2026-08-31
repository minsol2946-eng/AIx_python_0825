#1~100사이 랜덤 번호를 맞추는 프로그램 구현.
#랜덤번호< 내 번호<랜덤번호
#정답-정답숫자, 입력횟수, 입력숫자 출력
import random
RN=random.randint(1,100)
MN=[]
count=0
i=0
while True:
    no=int(input("숫자 입력: "))
    MN.append(no)
    i=i+1
    count=count+1
    if no>RN:print("입력한 수가 더 큽니다.")
    elif no<RN:print("입력한 수자 더 작습니다.")
    else: break

print("랜덤숫자: ",RN)
print("입력횟수: ",count)
print("입력숫자리스트: ",MN)
