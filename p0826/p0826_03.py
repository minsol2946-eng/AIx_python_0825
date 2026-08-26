num1=100
num2=100
num3=100
print(num1,num2,num3)

#한줄에 여러 변수에 한개값을 넣는 것은O
#한줄에 여러 변수에 여러개 값은 X
a1=1
a2=2
print(a1,a2)
#a1=1,a2=2  에러

a=100  #변수 선언
#== 같다는 뜻

a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b) #10*10*10 / 10 3승

# #print: 출력
# #input: 입력
# num=input("숫자를 입력하세요.")
# print("입력숫자:{}".fomat(num))

# #input으로 받은 모든 것은 문자열타입
# a = int(input("1번째 숫자를 입력하세요."))  #str타입을 int타입으로 변경
# b = int(input("2번째 숫자를 입력하세요."))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)


#아이디와 패스워드를 입력받아 출력하시오.
#아이디:aaa, 패스워드:1111
id=input("아이디를 입력하세요")
pw=input("패스워드를 입력하세요")
print("아이디확인:{}".format("aaa"==id))
print("패스워드확인:{}".format("1111"==pw))
print("아이디:{},패스워드:{}".format(id,pw))
