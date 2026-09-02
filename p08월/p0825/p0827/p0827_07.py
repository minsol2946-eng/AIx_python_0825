# 리스트는 []시작
# 리스트는 여러개를 저장
# 리스트는 0부터 주소가 시작
# 리스트를 print하면 모두 출력가능
# 리스트의 특정주소로 그 값을 출력할수 있음
# 리스트 개수 :len()
# 리스트 안에는 모든 타입을 넣을수 있음
# - 정수,실수,문자열,불,리스트,튜플,딕셔너리

# arr=[1,"안녕",1.2,True,[1,2,3]]
# print(arr[1])
# print(arr[3])
# print(arr[4])
# print(arr[4][1])
# a=arr[4]
# print(a[2])

# #1-10사이에 숫자 3개를 입력받아, 랜덤숫자를 맞추면 당첨 or not 꽝
# import random
# no1=int(input("첫번째 숫자 입력 "))
# no2=int(input("두번째 숫자 입력 "))
# no3=int(input("세번째 숫자 입력 "))
# print("입력한 숫자: ",no1,no2,no3)
# #반복문 사용 불가

# num=[0,0,0]
# num[0]=int(input("첫번째 숫자 입력 "))
# num[1]=int(input("두번째 숫자 입력 "))
# num[2]=int(input("세번째 숫자 입력 "))
# print("입력한 숫자: ",num)
# #리스트 사용은 반복문 사용 가능


# a="사과"
# b="딸기"
# c="수박"
# d="참외"
# e="복숭아"
# #a,b,c,d,e, 중 참외가 있는지 확인하고 확인 결과 출력.

# if a=="참외" or b=="참외" or c=="참외" or d=="참외" or e=="참외":
#     print("참외가 있습니다.")
# else: print("참외가 없습니다.")

# #리스트
# fruit=["사과","딸기","수박","참외","복숭아"]
# if "참외" in fruit:
#     print("참외가 있습니다.")
# else:
#     print("참외가 없습니다.")
#비교시 리스트는 ("검색내용" in 리스트)

# import random
# r_num=random.randint(1,10)
# #3개 숫자 입력
# arr=[]
# #리스트에 값을 추가: append
# arr.append(int(input("1. 1-10 숫자입력 : ")))
# arr.append(int(input("2. 1-10 숫자입력 : ")))
# arr.append(int(input("3. 1-10 숫자입력 : ")))
           
# print(arr)
# #1
# if r_num in arr:
#     print("당첨")
# else:
#     print("꽝")
# # 2
# if r_num in arr: print("당첨")
# else: print("꽝")
# # 3
# print("당첨") if r_num in arr else print("꽝")


# arr=["사과","딸기","수박","참외","복숭아"]
# print(arr[2])
# print(arr[1:4])     #1,2,3까지
# print(arr[2:])      #2~끝까지
# print(arr[:3])      #처음부터 3번까지
# print(arr[::2])     #[시작:끝:간격] ->사과,수박,복숭아

# #슬라이싱[시작:끝:간격]
# no=[1,2,3,4,5,6,7,8,9]
# print(no[::2])  #홀수만 추출
# print(no[1::2]) #짝수만 추출
# print(no[:-1])  #마지막 제외
# print(no[::-1]) #역순으로 출력

# #문자열-리스트 형태로 저장
# sentence="안녕하세요반갑습니다"
# print(sentence)
# print(sentence[6])
# print(sentence[5:8])
# print(sentence[::2])
# if "하"in sentence:
#     print("O")
# else:
#     print("X")

# #리스트+리스트
# arr1=[1,2,3]
# arr2=[4,5]
# print(arr1+arr2)
# arr3=arr1+arr2
# print(arr3)

# #리스트 * = 반복
# aaa=[0,0,0,0,0]
# aaa2=[0]*5
# print(aaa)
# print(aaa2)

# #리스트 추가: append,insurt
# #append 맨 뒤에 추가
# arr=[1,2]
# arr.append(3)
# arr.append(9)
# arr.append(5)
# #insult 원하는 위치 설정 후 추가
# arr.insult(1,20) #첫번째 자리에 20을 넣어라.
# #extend:원본 변형
# a=[1,2,3]
# b=[4,5,6]
# print(a+b)
# a.extend(b)
# print(a)

# #리스트 삭제: del, pop
# a=[1,2,3,4,5,"하하"]
# #pop으로 3 삭제
# a.pop(2)    #2번주소 지정
# print(a)
# #del
# del a[0]
# print(a)
# #remove: 지정 삭제
# a.remove("하하")
# print(a)

# #정렬-sort:순차 정렬, sort(reverse=True):역순 정렬
# arr=[4,8,48,65,12,6]
# arr.sort()
# print(arr)
# arr.sort(reverse=True)
# print(arr)

#리스트에 있는지 확인
arr=[3,4,5,6,7,8,9]
if 7 in arr:
    print("7이 있습니다.")
else:
    print("7이 없습니다.")

if not 5 in arr:
    print("5 없습니다.")
else:
    print("5 있습니다.")
