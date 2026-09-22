class Stu:
    def __init__(self,no,name,kor,eng,math): # 정보
        self.no=no
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=(kor+eng+math)/3

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.1f}"

    def total2(self): # 합
        self.total=self.kor+self.eng+self.math

    def avg2(self): # 평균
        self.avg=self.total/3

    # def print(self): #출력
    #     self.print=self.no,self.name,self.kor,self.eng,self.math,self.total,self.avg


#-----------------------------------------------------------------------------------------------
class Stu2:
    slist=[]

    def __init__(self,s):
        self.slist.append(s)

    def add(self,s):
        self.slist.append(s)
#-----------------------------------------------------------------------------------------------

p=Stu2(10,"짹짹이",20,30,40)
p.add(Stu(11,"멍멍이",50,80,70))

for ss in p.slist:
    print(ss)


while True:
    no=input("번호: ")
    name=input("이름: ")
    kor=int(input("국어: "))
    eng=int(input("영어: "))
    math=int(input("수학: "))
    slist.append(Stu(no,name,kor,eng,math))

    for s in slist:
        print(Stu(no,name,kor,eng,math))