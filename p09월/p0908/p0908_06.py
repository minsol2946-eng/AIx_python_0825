class People:
    # no=0
    # name=""
    # kor=0
    # eng=0
    # math=0

    def __init__(self,no,name,kor,eng,math): 
        self.no=no
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=(kor+eng+math)/3

    #출력 형식 함수
    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.1f}"

    def cal_total(self): 
        self.total=self.kor+self.eng+self.math

    def cal_avg(self): 
        self.avg=self.total/3

s1=People(1,"멍멍이",80,80,80)
s2=People(2,"야옹이",80,40,100)
s3=People(3,"꿀꿀이",100,50,20)


#출력: 참조변수명.변수명
print(s1)
print(s2)
print(s3)
#수정:참조변수명.변수명=수정값 >> 멍멍이 수학점수 수정
s1.math=90
s1.cal_total()
s1.cal_avg()
print(s1)