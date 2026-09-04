#######예외처리######
#try-except

# arr=[1,2,3,4,5]
# while True:
#     choice=int(input("0-4 숫자입력: "))
#     print("선택값: ",arr[choice])
    # try:
    #     choice=int(input("0-4 숫자입력: "))
    #     print("선택값: ",arr[choice])
    # except Exception as e:
    #     print("!!Error")
    #     print(e)
# print(0)
# try:
#     print(1)
#     print(2)
#     print(10/0) #에러
#     print(4)
# except Exception as e :
#     print(e)
#     print(type(e))
#     print(6)
#     print(7)
# print(8)


# print(1)
# print(2)
# print(3)
# print(4)
# raise NotImplementedError
# print(5)
# print(6)
# print(7)


#####raise######
#에러를 만들어 실행을 멈춘다.
#프로그램 구현이 안돼는 부분을 확인.

# choice=int(input("원하는 번호 입력: "))
# if choice==1:
#     print('학생성적입력')
# elif choice==2:
#     print("출력")
# elif choice==3:
#     ("수정")
# elif choice==4:
#     raise NotImplementedError   