import os
# print("운영체제: ",os.name)
# print("현재폴더: ",os.getcwd()) #현재폴더
# print("폴더 안 요소: ",os.listdir())    #폴더 안 요소
# os.mkdir("abc")

hello=open("hello.txt","r",encoding="utf-8")

while True:
    str=hello.readline()
    if str=="":break
    print(str,end="")
hello.close()
