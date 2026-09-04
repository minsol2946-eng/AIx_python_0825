#######예외처리######
#try-except

arr=[1,2,3,4,5]
while True:
    choice=int(input("0-4 숫자입력: "))
    print("선택값: ",arr[choice])
    # try:
    #     choice=int(input("0-4 숫자입력: "))
    #     print("선택값: ",arr[choice])
    # except Exception as e:
    #     print("!!Error")
    #     print(e)