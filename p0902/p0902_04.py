# #번호 3개를 받아  합을 구해서 출력하세요.
# str=input("번호 3개를 입력하세요.(22/33/44): ")
# str_list=str.split("/")
# print(str_list)
# sum=0
# for i in str_list:
#     sum+=int(i)
# print(sum)

# #map(함수,반복리스트)
# aa=['1','2','3']
# print(list(map(int,aa)))  #->문자열을 정수 타입으로 변경

# #map,join ->문자열
# stu=[1,"홍길동", 100,100,100]
# #,로 구분해서 문자열로 저장하시오.
# stu2=",".join(stu)
# print(stu2)
# print(list(map(str,stu)))   #특정한 함수로 반복해줌

#split 분리, *전개 연산자
str=input("날짜를 입력하세요.(2026/99/99): ")
str_arr=str.split("/")
print("{}년 {}월 {}일".format(*str_arr))