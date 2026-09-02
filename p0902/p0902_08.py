import random

def ran_num(choice):
    if choice==1:
        result=random.sample(range(1,100,5))
    elif choice==2:
        result=random.sample(range(1,100,3))
    else:result=random.sample(range(1,100,1))
    return result

def main_print():
    print("1.랜덤 숫자 5개")
    print("1.랜덤 숫자 3개")
    print("1.랜덤 숫자 1개")
    choice=int(input("원하는 번호 선택>> "))

#----------------------------------------------------------
while True:
    main_print()
    result=ran_num(choice)
    print("값: ",result)