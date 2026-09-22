#구매 총 금액 선택

com=print("1.컴퓨터:1_000_000")
lun=print("2. 세탁기: 2_000_000")
odi=print("3. 오디오: 5_000_000")

choice=input("원하는 번호와 개수를 입력(1/3): ") #str 문자열

def cal():
    choice2=choice.split("/")
    choice2=int(choice[0])
    choice2=int(choice[1])

    if choice2[0]=="1": #문자열로 비교
        print("컴퓨터")
        total=choice2[1]*1000000
        print("금액: ",total) #형 변환

    elif choice2[0]=="2":
        print("세탁기")
        total=choice2[1]*2000000
        print("금액: ",total)
    else:
        print("오디오")
        total=choice2[1]*5000000
        print("금액: ",total)      


#앞 숫자 *10/뒷 숫자*100 의 합계 구하기
num=(input("숫자 입력(1/1): "))
num2=num.split("/")


total=(int(num2[0])*10)+(int(num2[1])*100)
print("합: ",total)