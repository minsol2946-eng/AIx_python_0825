
# #open()파일 읽어오기
# # readFile=open("c:/aaa/abc.txt","r")


# # while True:
# #     str=readFile.readline()
# #     if str=="":break
# #     print(str,end="")

# # readFile.close()

# # print("프로그램 종료.")



# #with 파일 읽어오기
# with open("c:/aaa/abc.txt","r",encoding="utf-8") as f:  #한글 읽어 올 시: encoding="utf-8"
#     while True:
#         str=f.readline()
#         if str=="":break
#         print(str,end="")


# #stu 텍스트 읽어오기

# stuList = []
# with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:
#     while True:
#         str = f.readline()
#         if str == "": break
#         stu = str.split(",") #,기준으로 리스트생성
#         for i,s in enumerate(stu): # 1,홍길동,100,100,100,300,100.0
#             if 0<=i<=1: continue
#             elif 2<=i<=5:
#                 stu[i] = int(s.strip())  # s[i] = 문자열 1글자
#             elif i==6:
#                 stu[i] = float(s.strip()) # /n

#         stuList.append(stu)

#     print("파일읽어오기 완료")
#     print(stuList)




# sum=0
# with open("c:/aaa/aaa.txt","r",encoding="utf-8") as f:
#     while True:
#         str=f.readline()
#         if str=="":break
#         if str.strip().isdigit():
#             str=int(str)
#             sum+=str
#         print(str,end="")

# print("합계: ",sum)

with open("c:/aaa/abc.txt","r",encoding="utf-8") as f:
    while True:
        str = f.readline()
        if str == "": break
        print(str,end="")