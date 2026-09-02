#1-100까지 랜덤숫자 3개를 만들어서, 입력한 숫자 1개가 있는지 확인, 있으면 당첨 없으면 꽝
#랜덤 숫자 리스트, 입력 숫자 출력
import random

random_no1=random.randint(1,100)
random_no2=random.randint(1,100)
random_no3=random.randint(1,100)
total=[random_no1,random_no2,random_no3]
no1=int(input("숫자 입력: "))

if no1 in total:
    print("당첨 되셨습니다.")
else:
    print("다음 기회에...")

print("랜덤 숫자: ",total)
print("입력한 숫자: ", no1)

#aaa=random.sample(range(1,101),3)