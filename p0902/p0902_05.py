#함수####
# def fun():
#     print("함수를 호출 합니다.")

# def cal():
#     num1=int(input("숫자입력: "))
#     num2=int(input("숫자입력: "))
#     print(num1+num2)
#     print(num1-num2)
#     print(num1*num2)
#     print(num1/num2)

#함수 사용 이유: 긴 구문의 반복적인 명령어를 줄일 수 있음.


def stu_print():
    for s in stu: print("{} {} {} {} {}".format(*s))

stu=[
    [1,"홍길동", 90, 90, 90],
    [2,"유관순", 87, 88, 95],
    [3,"이순신", 96, 89, 93]
]

while True:
    print("1.학생성적입력")
    print("1.학생성적출력")
    print("1.학생성적검색")
    choice=int(input("원하는 번호를 입력하세요."))
    if choice==1:
        name=input("이름을 입력하세요.")
        stu_print()    
    elif choice==2:
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        stu_print()
    else:
        name = input("이름을 입력하세요.")
        stu_print()
        