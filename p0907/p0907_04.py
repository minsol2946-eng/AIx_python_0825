# #common폴더 안에 stu.txt로 파일을 저장하세요.
# #1 홍길동 100 100 100 300 100.0

# import os

# fname=input("파일 이름: ")

# # if not os. path.exists():

allStr = ""
no=0

with open("common/stu.txt","a",encoding="utf-8") as f:
    while True:
        outStr = input("내용입력 : ")
        if no==0:
            allstr=outStr
            no+=1
            continue
        if outStr == "":
            f.write(allStr+"\n")
            break
        allStr += (","+outStr)
        no+=1
    print(allStr)