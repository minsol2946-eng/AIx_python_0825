
#합 열번 반복

for i in range(10):
    num=int(input("숫자를 입력하세요>>"))
    sum=0
    for i in range(1,11):
        sum+=i
    print(sum)

#---------------------------------------------

def add():
    num=int(input("숫자를 입력하세요>>"))
    sum=0
    for i in range(1,11):
        sum+=i
    print(sum)

for i in range(10):
    add()

#-----------------------------------------------

def add2(num2):
    sum=0
    for i in range(1,num2+1):
        sum+=i
    print(add2)

for i in range(10):
    num2=int(input("숫자를 입력하세요>>"))
    add2(num2)


#-----------------------------------------------

def add3(num3,num4):
    sum=0
    for i in range(num3+num4+1):
        sum+=i
    return sum    #출력을 for문에서 하고 싶을 때

for i in range(10):
    num3=int(input("숫자를 입력하세요>>"))
    num4=int(input("숫자를 입력하세요>>"))
    sum=add3(num3,num4)
    print(add3)

