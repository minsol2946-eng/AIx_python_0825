
# 구구단을 아래로 출력하시오.
# for i in range(2,10):
#     print(f"[{i}단]",end="\t")
# print()
# for i in range(1,10):
#     for j in range(2,10):
#         print("{}x{}={}".format(j,i,i*j),end='\t')
#     print()

# sum=0
# result=1
# for i in range(1,11):
#     sum=sum+i
#     result=result*i
#     if result>=100:
#             print(i,',',result)
#             break # 강제종료

# print("합계: ",sum)
# print("곱: ",result)

#1-100까지의 합을 구하세요.

# sum=0
# for i in range(1,101):
#     sum=sum+i

# print("합: ",sum)

# #홀수만 구하기
# sum=0
# for i in range(1,101,2):
#     sum=sum+i

# print("홀수 합: ",sum)

# #7의 배수 합
# for i in range(1,101):
#     if i%7==0:print("홀수 합: ",i)
#     sum=sum+i
# print(sum)

# #3개의 입력한 숫자의 합을 구하시오.
# sum=0
# for i in range(3):
#     no=int(input("숫자 입력: "))
#     sum=sum+no
# print("합: ",sum)

# #리스트 추가
# list=[]
# for i in range(3):
#     no2=int(input("숫자 입력: "))
#     list.append(no2)
#     sum=sum+no2
# print("합계: ",sum)
# print("입력 값: ",list)


# #첫번재 입력한 숫자부터, 두번째 입력한 숫자까지 합을 구하세요
# sum=0
# c=0
# a=int(input("숫자입력: "))
# b=int(input("숫자입력: "))
# if a>b: #a가 b보다 값이 큰 경우 사용.
#     a,b=b,a
# for i in range(a,b+1):
#     sum=sum+i
# print("합: ",sum)


# #구구단 출력
# #입력받아 그 숫자 단부터 출력
# j=int(input("시작 단 입력:"))
# l=int(input("끝 입력:"))
# for i range(j,j+1):
#     for k range(1,l+1):
#         print:(f"{j}x{k}={j*k}")

# list_a=["바나나","딸기","사과"]
# for i in range(3):
#     list_a.append(input("과일: "))

# for i in list_a:
#     print(i)

# list_a=["바나나","딸기","사과"]
# j=1
# for i in list_a:
#     print(j,".",i)
#     j=j+1

# for i,value in enumerate(list_a):   #enumerate: index번호, 리스트값 2개 전달.
#     print(i+1,".",value)

# for i in range(len(list_a)):
#     print(i+1,".",list_a[i])


#3명 이름 성적 받기
name=[]
kor=[]
eng=[]
math=[]
total=[]
avg=[]
for i in range(3):
    name.append(input("이름: "))
    k_in=(int(input("국어 점수: ")))
    kor.append(k_in)
    e_in=(int(input("영어 점수: ")))
    eng.append(e_in)
    m_in=(int(input("수학 점수: ")))
    math.append(m_in)
    total.append(k_in+e_in+m_in)
    avg.append(k_in+e_in+m_in/3)

print("[학생 성적 점수]")
ptint("번호\t이름\t국어\t영어\t수학\t전체\t평균")
for i in range(len(name)):
    print(f"{name[i]},/t{kor[i]},/t{eng[i]},/t{math[i]},/t{total[i]},/t{avg[i]}")


# name = []
# kor = []
# eng = []
# math = []
# total = []
# avg = []
# for i in range(3):
#     name.append(input("이름입력 :"))
#     k_input = int(input("국어점수입력 : "))
#     kor.append(k_input)
#     e_input = int(input("영어점수입력 : "))
#     eng.append(e_input)
#     m_input = int(input("수학점수입력 : "))
#     math.append(m_input)
#     total.append(k_input+e_input+m_input)
#     avg.append((k_input+e_input+m_input)/3)

# print("[ 학생성적 ]")
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t")
# print("-"*60)
# for i in range(len(name)):
#     print(f"{i+1}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\
# \t{total[i]}\t{avg[i]:.2f}")