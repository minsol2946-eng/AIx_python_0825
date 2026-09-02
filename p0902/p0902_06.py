# def print1():
#     print("Hello")
#     print("Hello")
#     print("Hello")

# print1()


#함수:1.긴 구문 반복사용 시/ 2.프로그램을 간경하게 하기 위해

#def 이름()



# 학생성적
stu = [
    # {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100},
    # {},
    # {}
]
c_no=0

def main_print():   #메인 출력
    print("[ 학생성적프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("-"*60)

def stu_input():
    c_no = 1   #학생번호로 사용
    print()
    while True:
        print("[ 학생성적입력 ]")
        no = c_no
        name = input("학생이름입력 (0.이전페이지 이동) : ")
        if name=="0": break
        kor = int(input("국어점수입력 : "))
        eng = int(input("영어점수입력 : "))
        math = int(input("수학점수입력 : "))
        total = kor+eng+math
        avg = total/3
        stu.append(
            {"no":no,"name":name,"kor":kor,"eng":eng\
            ,"math":math,"total":total,"avg":avg}
        )
        print(name,"학생 성적이 저장되었습니다.")
        c_no += 1   # 다음번호 1증가
    print()

# 화면출력
# 1. 성적입력
# 2. 성적출력
c_no = 1   #학생번호로 사용
while True:
    main_print()
    choice = int(input("원하는 번호를 입력하세요."))
    if choice == 1:
        
    elif choice == 2:
        print()
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\
\t{s['eng']}\t{s['math']}\t{s['total']}\
\t{s['avg']:.2f}")
        print()