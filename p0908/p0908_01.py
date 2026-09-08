################clss(클래스): 묶음으로 통합 관리.##################
#변수화 함수를 모구 포함해서 구현.
#관리가 용이.
#다른 것과 헷갈릴 일 X

class Car:
    color=""
    speed=0
    tire=0
    door=0

    ##생성함수
    def __init__(self,color,speed,tire,door):
        self.color=color
        self.speed=speed
        self.tire=tire
        self.door=door

    def upspeed(self):
        self.speed+=10

    def downspeed(self):
        self.speed-=10

#클래스 1개 생성
c=Car()     #객체생성(인스턴스생성)
# c.color="white"
# print(c.color)
# print(c.speed)

# c.upspeed()
# print(c.upspeed)

#ex) c2=Car(),c3=Car()

c=Car()     #4개 변수, 2개 함수 생성.
c.color="black" #지정 클래스를 찾아가 입력.
c.speed=100
c.tire=4
c.door=3

c2=Car()
c.color="blue"
c2.speed=200
c2.tire=4
c2.door=5

#클래스 객체 선언
c3=Car("gray",70,4,4)
c.color="gray"
c.speed=70
c.tire=4
c.door=4