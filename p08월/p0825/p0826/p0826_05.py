# #번호, 이름, 국어, 영어, 수학 을 입력받아 합계와 평균을 출력.
# no=input("번호를 입력하시오.")
# name=input("이름을 입력하시오.")
# kor=int(input("국어 점수를 입력하시오."))
# eng=int(input("영어 점수를 입력하시오."))
# math=int(input("수학 점수를 입력하시오."))

# total=kor+eng+math
# avg = total/3
# print("-"*80)
# print("번호{},이름{},합계 점수{},평균 점수{:.1f}".format(no,name,total,avg))
# print("-"*80)


# no2=input("번호를 입력하시오.")
# name2=input("이름을 입력하시오.")
# kor2=int(input("국어 점수를 입력하시오."))
# eng2=int(input("영어 점수를 입력하시오."))
# math2=int(input("수학 점수를 입력하시오."))
# total2=kor+eng+math
# avg2= total/3
# print("-"*80)
# print("번호\t 이름\t 국어\t 영어\t 수학\t 합계점수\t 평균점수\t")
# print("-"*80)
# print("{}\t {}\t {}\t {}\t {}\t {}\t {:.1f}".format(no2,name2,kor2,eng2,math2,total2,avg2))
# print("-"*80)

a=10
a=a+2
a+=2

#원의 반지름을 입력받아 원의 넓이를 출력하시오.
#파이 *반지름*반지름
#원의 넓이 100cm2

length=int(input("반지름을 입력하세요."))
pi=3.14
result=pi*(length**2)
print("반지름: {:.2f}".format(result))


#원의 둘레

print("원의 둘레: {}".format(2*pi*length))
# 원의 둘레 : cm
print("원의 둘레 : {:.2f}".format(result2))