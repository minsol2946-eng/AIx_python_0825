class Stu:
    def __init__(self,no,name,kor,eng,math): # 정보
        self.no=no
        self.name="name"
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=(kor+eng+math)/3

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\
            \t{self.total}\t{self.avg}"

    def total(self): # 합
        self.total=self.kor+self.eng+self.math

    def avg(self): # 평균
        self.avg=self.total/3

    def print(self): #출력
        self.print=self.no,self.name,self.kor,self.eng,self.math,self.total,self.avg

s=Stu(1,"멍멍이",60,70,80)
s.print()
print(s)








#----------------------------------------------------------------------------
class Stu2:
    def __init__(self,no,name,kor,eng,math):
        self.__no2=no           ## __ 캡슐화:클래스 내에서만 수정 가능
        self.__name2="name"
        self.__kor2=kor
        self.__eng2=eng
        self.__math2=math
