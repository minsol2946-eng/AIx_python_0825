# #날짜 함수, 랜덤 함수
# import datetime
# import random
# now=datetime.datetime.now()
# print(now)
# print(now.year)
# print(now.month)

# #랜덤함수
# import random
# r_num=random.randint(1,12)
# #4계절로 나누기
# print(r_num)
# if 3<=r_num<=5:print("spring")
# elif 6<=r_num<=8:print("summer")
# elif 9<=r_num<=11:print("fall")
# else:print("winter")

#랜덤 5개
# randint-랜덤1개    sample-랜덤여러개(중복불가),
# shuffle-전체섞음    choices-랜덤여러개(중복가능)

import datetime
import random

# # alist=[0,0,0,0,0]
# # alist2=[0]*5
# # alist3=list(range(1,6))
# # print(alist)
# # print(alist2)
# # print(alist3)

# a=random.randint(1,45)      #랜덤1개
# arr=random.sample(range(1,46),5)     #1-45중 중복없이 5개
# print(arr)
# arr2=random.sample([50,99],2)
# print(arr2)

# arr3=[1,2,3,4,5,6,7,8,9]
# random.shuffle(arr3)        #랜덤으로 섞음
# print(arr3)

# arr4=[4,5,6,7,8,9,10,11]
# arr5=random.choices(arr4,k=4)       #중복가능
# print(arr5)


#1-45까지 랜덤 5개를 가져와서, 입력한 숫자가 있으면 당첨, 없으면 꽝

lotto=random.sample(range(1,46),5)
input1=int(input("1.숫자 입력: "))
input2=int(input("2.숫자 입력: "))
input3=int(input("3.숫자 입력: "))
input4=int(input("4.숫자 입력: "))
input5=int(input("5.숫자 입력: "))
tt=input1,input2,input3,input4,input5

if tt in lotto: print("당첨!!")
# if input2 in lotto: print("당첨!!")
# if input3 in lotto: print("당첨!!")
# if input4 in lotto: print("당첨!!")
# if input5 in lotto: print("당첨!!")
else:print("꽝ㅠㅠ")