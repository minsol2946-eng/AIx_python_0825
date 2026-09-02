#
import random
ranNum=random.sample(range(1,11),1)
def main():
    print("1. 구구단 출력 프로그램")
    print("2. 1~10까지 숫자 맞추기 프로그램")
    print("3. 두 수를 입력받아 +,-,*,/의 결과값")
    choice=int(input("원하는 번호 입력: "))
    return choice

def pro1():
        for i in range(1,10):
            for j in range(2,10):
                print("{}x{}={}".format(j,i,i*j),end='\t')

def pro2():
        myNum=int(input("1~10중 선택하여 입력>>> "))
        if myNum in ranNum:
            print("딩동댕")    
        else:print("땡")

def pro3():        
    num1=int(input("숫자를 입력>>> "))
    num2=int(input("숫자를 입력>>> "))
    str=input("사칙연산 선택>>>  ")
    result=0
    if str=="+":result=num1+num2
    elif str=="-":result=num1-num2
    elif str=="*":result=num1*num2
    elif str=="/":result=num1/num2
    print(result)

#------------------------------------------------------------
while True:
    choice=main()
    if choice==1:
        pro1()
    elif choice==2:
        pro2()
    else:
        pro3()