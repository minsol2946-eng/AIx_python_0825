# money=12340
# #500원 동전 몇개가 필요할까요?
# result=money//500
# print("500원 동전의 갯수{}".format(result))
# result2=money//100
# print("100원 동전의 갯수{}".format(result2))

# #12340원->500원동전 몇개? 100원 몇개? 10원 몇개?

# result1=money//500
# num1=money%500

# result2=(result1)//100
# num2=num1%100

# result3=(result2)//10
# num3=num2%10
# print("-"*60)
# print("500원 갯수:{}, 나머지{}\n" \
# "100원 갯수:{}, 나머지{}\n" \
# "10원 갯수{}, 나머지{}".format(result1,num1,result2,num2,result3,num3))


#관계연산자: ==,!=,>,<,>=,<=
#True, False bool타입으로 반환

#아이디, 패스워드를 입력받아 맞는지 확인.
#아이디:aaaa, 패스워드:1111
# id=input("아이디를 입력하시오.")
# pw=input("비밀번호를 입력하시오.")
# if (id=="aaaa") and (pw=="1111"):
#  print("로그인이 되어 메인페이지로 이동합니다.")
# else:
#  print("아이디 또는 비밀번호가 일치하지 않습니다.")

#프로그램 종료
#대문자 X 또는 x 입력하면 종료
str1=input("프로그램을 종료하려면 X 또는 x를 입력하세요.")
if(str1=="X") or (str1=="x"):
  print:("프로그램을 종료합니다.")
else:
  print("프로그램을 계속 실행합니다.")