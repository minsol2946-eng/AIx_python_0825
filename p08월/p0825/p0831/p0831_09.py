#LOTTO PLAYING
import random
lotto=random.sample(range(1,46),6)
MN=[]
i=0
while i<6:
    no=int(input("입력: "))
    if no not in lotto:
        MN.append(no)
        i=i+1
    else:print("중복된 번호 입니다.")

match=[]
count=0
for i in MN:
    if i in lotto:
        count=count+1
        match.append(i)

print("Lotto: ",lotto)
print("My: ",MN)
print("How many: ",count)
print("Matched: ",match)