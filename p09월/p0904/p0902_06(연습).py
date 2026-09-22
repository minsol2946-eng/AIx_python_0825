#text2.txt 파일을 읽어와서
#stu=[]에 저장
stu=[]
file=open("C:/aaa/test2.txt","r",encoding="utf-8")

while True:
    line=file.readline()
    if line=="":break
    line=line.strip()
    print(line,end="")
    arr=line.split(",")
    for i,a in enumerate(arr):
        if 5>=i>=2:arr[i]=int(a)
        elif i==6:arr[i]=float(a)
    stu.append({"no":arr[0],"name":arr[1],"kor":arr[2],"eng":arr[3],"math":arr[4],"total":arr[5],"avg":arr[6]})

file.close()