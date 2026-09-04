
title=["번호","이름","국어","영어","수학","합계","평균"]
k_title=["no","name","kor","eng","math","total","avg"]
stu=[]
sno=1 #학생성적인원변수 -db

#####함수선언#####

def s_mainprint():  #메인화면
    print("[학생 성적 프로그램]")
    print("1.성적 입력")
    print("2.성적 출력")
    print("3.성적 검색/수정")
    print("-"*60)
    choice=int(input("원하는 번호 입력>> "))
    return choice

def s_input(): #성적 입력 
    global sno
    while True: #성적 입력
        no=sno
        print("[학생 성적 입력]")
        name=input(f"{no}번째 이름 입력: ")
        if name == "0": break
        kor=int(input("국어 점수: "))
        eng=int(input("영어 점수: "))
        math=int(input("수학 점수: "))
        total=kor+eng+math
        avg=total/3

        stu.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
        print(f"{name}학생 성적이 저장 되었습니다.")
        print()
        # score=[0]*3
        # for i in range(3):
        #     score[i]=int(input(f"{title[i+2]} 점수 입력: "))

        sno+=1

def s_output(): #성적 출력 함수
    print()
    print("[성적 출력]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
    print("-"*60)
    if len(stu)==0:
        print("데이터가 없습니다.")
    else:
        for s in stu:
            print(f"{s["no"]}\t{s["name"]}\t{s["kor"]}\t{s["eng"]}\t{s["math"]}\t{s["total"]}\t{s["avg"]:.2f}\t")


def s_update():
    print("[ 성적 수정 ]")
    name=input("학생 이름 검색>>")
    temp=0
    for i,s in enumerate (stu):
        if s ["name"]==name:
            print(f"{name}학생을 찾았습니다.")
            temp=1
            break

    if temp == 0:
        print(f"{name} 학생이 없습니다.")
    elif temp == 1:
        print("[ 과목수정선택 ]")
        print("1. 국어   2. 영어   3. 수학")
        choice = int(input("원하는 번호입력 : "))

        print(f"현재{title[choice+1]}점수 : {s[k_title[choice+1]]}")
        s[k_title[choice+1]] = int(input(f"변경하려는 {title[choice+1]}점수 : "))
        s['total'] = s['kor']+s['eng']+s['math']
        s['avg'] = s['total']/3
        print(f"{s[k_title[choice+1]]}점으로 {title[choice+1]}점수가 변경되었습니다.")

#-----------------------------------------------------------------------------------
while True:
    choice=s_mainprint()    #메인화면 부분 함수 호출
    print()

    if choice==1:   #성적 입력
        sno=s_input()
        s_output()

    elif choice==2: #성적 출력
        s_output()
    elif choice==3: #학생 성적 수정
        s_update()