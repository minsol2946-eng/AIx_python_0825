

print("1.구구단 출력")
print("2.두 수를 입력받아, +,- 값 구하기")
print("3. 1~10까지 합을 출력")

choice=int(input("번호 선택>>> "))

def gugudan():
    for i in range(2,10):
        for j in range(1,10):
            print(f"{i}x{j}={i*j}",end='\t')

def plus_minus():
    num1=int(input("숫자 입력: "))
    num2=int(input("숫자 입력: "))
    print(num1+num2)
    print(num1-num2)

def sum():
    sum2 =0
    for i in range(1,11):
        sum2 += i
    print("합: ",sum2)



if choice==1:
    gugudan()
elif choice==2:
    plus_minus()
else:
    sum()