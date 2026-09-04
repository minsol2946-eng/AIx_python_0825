
# myInfo = {"id":"aaa","pw":"1111","name":"홍길동","money":10000000}

# s_arr = [
#     {"prd_name":"컴퓨터","price":1000000},
#     {"prd_name":"냉장고","price":2000000},
#     {"prd_name":"오디오","price":500000},
#     {"prd_name":"세탁기","price":1500000}
#     ] # 1-0,2-1,3-2
# # s_arr[0]   s_arr[0]['prd_name']

# def cal(choice):
#     if myInfo['money']<s_arr[choice-1]['price']:
#         print("잔액이 부족합니다.")
#         return
#     print(f"구매상품:{s_arr[choice-1 ]["prd_name"]}")
#     print(f"상품금액:{s_arr[choice-1]["price"]}")
#     myInfo['money'] -= s_arr[choice-1]['price']
#     print(f"구매 후 잔액: {myInfo['money']:,}원")
    


# # print("1.컴퓨터") #s_arr[choice-1 ]["prd_name"],s_arr[choice-1]["price"]
# # print("2.냉장고") # s_arr[1]["prd_name"]
# # print("3.오디오")
# # print("4.세탁기")

# for i,V in enumerate(s_arr):
#     print(f"{i+1}.{V["prd_name"]}:{V["price"]}")

# while True:
#     choice = int(input("원하는 번호입력 : "))
#     if choice == 1:
#         cal(choice)
#     elif choice == 2:
#         cal(choice)
#     elif choice == 3:
#         cal(choice)
#     elif choice == 4:
#         cal(choice)



mI={"id":"minsol","pw":"4321","money":50000}
product=[
    {"p_n":"비비빅","price":2000} 
    {"p_n":"요맘때","price":1500}
]

def cal(choice):
    print(f"구매상품: {product[choice-1]["p_n"]} ")
    print(f"상품금액: {product[choice-1]["price"]} ")
    print("구매 후 잔액: ")
    print("잔액부족.충전 후 결제 요청")

for i,v in enumerate(product):
    print(f"{i+1},{v["p_n"]}:{v["price"]}")



while True:
    if choice==1:
        cal(choice)
    else:
        cal(choice)