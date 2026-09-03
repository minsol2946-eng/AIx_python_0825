
# def func1():
#     a=10    #지역변수
#     print("func1 a: ",a)

# def func2():
#     print("func2 a: ",a)

# a=20    #전역변수

# func1()
# func2()


# def func1():
#     global a    #전역변수에 선언되어 있는 링크를 가져옴
#     a=10
#     print("func1a: ",a)

# a=20
# func1()
# print("전역변수: ",a)

# def func1(a,b,c):
#     print(a)
#     return a+10

# c=30
# result=func1(10,2,c)
# print(result)


def func1(num1,num2,*num3):
    sum=num1+num2
    for n in num3:
        sum+=n
    return sum

print(func1(1,2,3))
print(func1(11,12,13,14))

#2~10개까지 몇개를 매개 변수로 사용하든지 합계를 구하도록

# def para_func(num,*num2):
#     sum=num+num2
#     for 

# print(para_func(10,20,30,40))


# import func
# func.cal1()

# from func import cal2()

