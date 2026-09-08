class Student:
    # no=0
    # name=""
    # kor=0
    # eng=0
    #클래스 내 함수 매개변수 첫번째(self)
    #생성자: 위의 변수를 만들지 않아도 인잇 함수로 가능.
    def __init__(self,no,name,kor,eng,math):     
        self.no=no
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=kor+eng+math/3

    def sum(self):
        self.sum=self.kor+self.eng+self.math

    def avg(self):
        self.avg=self.sum/3

    def print(self):
        print(self.no,self.name,self.kor,self.eng,self.math,self.total,self.avg,sep="\t")

stulist=[]

#객체선언
s=Student(1,"홍길동",100,100,99)
# stulist.append(s)

s.kor=50    #수정
s.math=100  #클래스에 변수 추가 생성
s.print()


#-----------------------------------------------------------------------------------------------
class Student2:
    # 생성자
    def __init__(self,no2,name2,kor2,eng2,math2):
        self.__no2 = no2
        self.__name2 = name2
        self.__kor2 = kor2  #캡슐화:클래스내부에서만 값을 수정
        self.__eng2 = eng2
        self.__math2 = math2
        self.__total2 = kor2+eng2+math2
        self.__avg2= (kor2+eng2+math2)/3

    def __str__(self):
        return f"{self.__no2}\t{self.__name2}\t{self.__kor2}\t{self.__eng2}\t{self.__math2}\t{self.__total2}\t{self.__avg2:.2f}"

    def get_kor(self):
        return self.__kor2

    def set_kor(self,kor):
        self.__kor2 = kor2


    # 클래스 내 함수 매개변수 첫번째 self
    def cal_total(self):
        self.__total2 = self.__kor2+self.__eng2+self.__math2

    def cal_avg(self):
        self.__avg2 = self.__total2/3

    def print(self):
        print(self.__no2,self.__name2,self.__kor2,self.__eng2,self.__math2,self.__total2,f"{self.__avg2:.2f}",sep="\t")

stuList = []
# 객체선언
s = Student(1,"홍길동",100,100,99)
print("-"*50)
print(s)
print("-"*50)
s.__kor2 = 70    # 클래스 변수값 수정
s.__math2 = 40   # 클래스 변수값 수정
s.set_kor2(-50)
s.cal_total2()
s.cal_avg2()
s.print2()
print(s)