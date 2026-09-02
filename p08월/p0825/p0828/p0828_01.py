#번호, 이름, 국어, 영어, 수학->합계,평균->성적출력
#입력->변수저장->성적출력

no=input("번호를 입력하세요.")
name=input("이름을 입력하세요.")
kor=int(input("국어 점수를 입력하세요.")) #kor=int(kor)
eng=int(input("영어 점수를 입력하세요."))
math=int(input("수학 점수를 입력하세요."))
total=kor+eng+math
avg=total/3

print("[학생 성적 프로그램]")
print("-"*65)
print("번호\t 이름\t 국어\t 영어\t 수학\t 합계\t 평균\t")
print("-"*65)
print("{}\t {}\t {}\t {}\t {}\t {}\t {:.2f}\t"\
       .format(no,name,kor,eng,math,total,avg))
print(f"{no}\t {name}\t {kor}\t {eng}\t {math}\t {total}\t {avg:.2f}\t") # 포멧함수
