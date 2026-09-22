import p09월.p0907.func as func

# hap() 함수
# def hap():
#     num1 = int(input("숫자입력1 : "))
#     num2 = int(input("숫자입력2 : "))
#     sum = num1+num2
#     print(sum)


#--------------------------------------------------------------

# 1. 매개변수X, return X - hap()
func.hap1()

#--------------------------------------------------------------

# 2. 매개변수 O, return X - hap2()

# def hap(num1,num2):
#     sum = num1+num2
#     print(sum)

num1 = int(input("숫자입력1 : "))
num2 = int(input("숫자입력2 : "))
sum = func.hap2(num1,num2)

print("프로그램 종료")

#--------------------------------------------------------------

# 3. 매개변수 O, return O - hap3()
# def hap3(num1,num2):
#     sum=(num1+num2)
#     return sum

num1 = int(input("숫자입력1 : "))
num2 = int(input("숫자입력2 : "))
sum = func.hap3(num1,num2)
print(sum)
print("프로그램 종료")