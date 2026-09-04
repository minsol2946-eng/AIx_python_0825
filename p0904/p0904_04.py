#######파일 읽어오기#####

f=open("C:/aaa/test1.txt","r",encoding="utf-8")

# f1=file1.readline
# print(f1,end="")
# f2=file1.readline
# print(f2,end="")
# f3=file1.readline
# print(f3,end="")

while True:
    line=f.readline()
    if not line:
        break
    print(line,end="")
f.close()