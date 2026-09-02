# ranNo=[1,5,9,7,4]
# inputNo=[1,2,3,4]
# answerNo=[]
# #입력한 숫자와 랜덤숫자가 몇개가 같은지 갯수를 출력.
# count=0
# for i in inputNo:
#     if i in ranNo:
#         count=count+1
#         answerNo.append(i)
#         print("있다.")
#     else:print("없다.")

# print("갯수: ",count)


#입력한 숫자를 모두 저장해서, 종료 시 출력.(0 입력시 종료: 입력한 수, 갯수 동시 출력)
noArr=[10,40,2,9,5]
answer=[]
no=[]
count=0
while True:
    i_no=int(input("숫자 입력: "))
    no.append(i_no)
    if i_no==0:
        count=count+1
        print(f"종료 합니다.\n입력한 숫자:{no}, 갯수:{count}")
        break

for i in no:
    if i in noArr:
        count=count+1
        answer.append(1)
print("리스트: ",noArr)
print("입력숫자: ",no)
print("맞춘 갯수: ",count)
