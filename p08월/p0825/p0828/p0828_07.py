# #format함수
# a=10
# print("{}".format(a))
# print("{:10d}".format(a))
# print("{:010d}".format(a))
# print("{:3,d}".format(100000000))

# #문자인지 아닌지 확인.
# #영문 이름 입력을 받는데,
# name=input("이름을 입력하시오.")
# if name.isalpha():print("문자로 돼있습니다.")
# else:print("이 외의 문자 입니다.")

# print(name)

#------------------------------------------------------

# num=input("숫자를 입력하세요. ")
# if num.isdigit():
#     num=int(num)
#     num+=100
#     print("입력숫자: ",num)
# else:print(num)
# num2=int(num)
# print("입력된 숫자: ", num2)
#--------------------------------------------------------
paper="""네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 
2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다.
이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서
비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."""

# result1=paper.find("홍수")
# result2=paper.rfind("홍수")
# result3=paper.count("홍수")
# print(result1)
# print(result2)
# print(result3)
#-------------------------------------------
# #in 함수
# if "방울" in paper:print("있음")
# else: print("없음")
#--------------------------------------------
#split()구분자로 분리
# str1="1,김민솔,100,100,99"
# s=str1.split(",")
# print(s[4])

#Q.str1 = "1,홍길동,100,100,99"
# 번호,이름,국어,영어,수학,합계,평균을 출력하시오.
# stu="1,홍길동,100,100,99"
# s=stu.split(",")
# s[2]=int(s[2])
# s[3]=int(s[3])
# s[4]=int(s[4])
# tt=int(s[2]+s[3]+s[4])
# avg=tt/3
# print("[학생성적프로그램]")
# print("-"*65)
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{tt}\t{:avg.2f}")
# print("-"*65)  #문자*반복

#선생님# 번호,이름,국어,영어,수학,합계,평균을 출력하시오.
str1 = "1,홍길동,100,100,99"
s = str1.split(",") #['1','홍길동','100','100','99'] - 문자열
s[2] = int(s[2]) # 국어
s[3] = int(s[3])
s[4] = int(s[4])
s.append(s[2]+s[3]+s[4]) # 합계추가
s.append(s[5]/3)         # 평균추가

print("[학생성적프로그램]")
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)  #문자*반복

# *s : 구조분해할당 (s[0],s[1],s[2],s[3],s[4],s[5],s[6])
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))
print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}")