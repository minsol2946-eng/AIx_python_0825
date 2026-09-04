title=["번호","이름","국어","영어","수학","합","평균"] #이름
key_title=["no","name","kor","eng","math","total","avg"] #점수
stu=[] #딕셔너리로 리스트 생성
sno=1



##################함수#################

def main():
    print("[  성적 프로그램  ]")
    print("1. 성적 입력")
    print("2. 성적 출력")
    print("3. 성적 검색 및 수정")   #if 문으로 초이스 3개
    print("-"*65)
    choice=int(input("원하는 번호 선택>>> "))    






#######################################

while True:     #메인
    # print("[  성적 프로그램  ]")
    # print("1. 성적 입력")
    # print("2. 성적 출력")
    # print("3. 성적 검색 및 수정")   #if 문으로 초이스 3개
    # print("-"*65)
    # choice=int(input("원하는 번호 선택>>> "))
    main()

    #성적 입력
    if choice==1:
        while True:
            no=sno  #sno리스트 만드는 이유??: 나중에 삭제시 미리 만들어 둔다.
            print("[ 성적을 입력 합니다. ]")
            name=input(f"{no}번째 이름: ")
            if name == "0":break
            kor=int(input("국어 점수: "))
            eng=int(input("영어 점수: "))
            math=int(input("수학 점수: "))
            total=kor+eng+math
            avg=total/3
            #리스트에 추가
            stu.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
            print(f"{name}학생의 성적이 저장되었습니다.")
    #출력
    elif choice==2:
        print("-"*60)
        print("[   성적표   ]")
        print("-"*60)
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title)) #리스트
        print("-"*60)
        if len(stu)==0:
            print("데이터가 없습니다.")
        else:
            for s in stu:   #s 사용 없이 *stu 하면 안되는지???/ 딕셔너리형태로 stu=[]리스트에 저장됨.
                print(f"{s["no"]}\t{s["name"]}\t{s["kor"]}\t{s["eng"]}\t{s["math"]}\t{s["total"]}\t{s["avg"]}\t")
    #수정
    else:
        print("[  검색 및 수정  ]")
        name=input("검색할 이름을 입력하세요>>> ")
        temp=0   #뭐더라?
        for i,s in enumerate(stu):
            if s ["name"]==name:
                temp=1
                break

            if temp==0:
                print(f"{name}의 데이터가 없습니다.")
            elif temp ==1:
                print("-"*60)
                print("[  수정 과목 선택  ]")
                print("1.국어   2.영어   3.수학")
                choice=int(input("과목 번호를 입력하세요>>> "))

            #점수 수정  k_title[choice+1]
            print(f"현재 {title[choice+1]}점수: {s[key_title[choice+1]]}")
            s[key_title[choice+1]]=int(input(f"변경 하려는 title[choice+1] 점수: "))
            s["total"]=s["kor"]+s["eng"]+s["math"]
            s["avg"]=s["total"]/3
            print(f"{s[key_title[choice+1]]} 으로 변경 완료.")