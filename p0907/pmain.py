from pfunction import*

stulist=[]
title=["번호","이름","국어","영어","수학","합계","평균","등수"]
s_title=["no","name","kor","eng","math","total","avg","rank"]
stuNum=1


#메인
def main():
    print("[성적 프로그램]")
    print("1. 성적 입력")
    print("2. 성적 출력")
    print("3. 성적 수정")
    print("9. 성적 파일 저장")
    print("0.프로그램 종료")
    print("-"*60)
    choice=int(input("원하는 번호 선택>>"))

#입력
def s_input():
    global stuNum   #stuNum=1불러오기 위함
    while True:
        print("성적 입력: ")
        no=stuNum
        name=input(f"{stuNum}번째, 학생이름: ")
        if name=="0":break
        kor=int(input("국어: "))
        eng=int(input("영어: "))
        math=int(input("수학: "))
        total=kor+eng+math
        avg=total/3
        rank=0
        stulist.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank,})
        print("성적이 저장 되었 습니다.")
        stuNum+=1

#출력
def s_output():
        print("[성적 출력]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*60)
        for s in stulist:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank'],}")
        print()

#성적파일불러오기
def readStu():
    global stuNum   #stuNum=1불러오기 위함
    with open("c:/aaa/stu.txt",'r',encoding="utf-8") as f:
        while True:
            str=f.readline()
            if str=="":break
            stu=str.split(",")
            for i,s in enumerate(stu): #(i번째,stu)
                if 0<=i<=1:continue
                elif 2<=i<=5:stu[i]=int(s.strip()) #정수로 저장하고 공백 제거
                elif i==6:stu[i]=float(s.strip())  #실수로 저장하고 공백 제거(평균점수)
                elif i==7:stu[i]=int(s.strip())  #등수
            stulist.append(dict(zip(s_title.stu)))  #dict:zip읽기/zip:두가지 묶기
            stuNum=len(stulist)+1   #??????????


#성적파일저장하기




while True:
    choice=int(input("원하는 번호 선택>>"))

    if choice==1:s_input()

    if choice==2:s_output()

    if choice==3:pass
    if choice==9:pass