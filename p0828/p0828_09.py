
# #반복문: for 변수 in 범위:

# for i in range(10):
#     print(i)
# for i in range(5):
#     print(i*10)
# for i in range(0,10,2):
#     print(i)
# for i in [5,3,6,2]:
#     print(i)

# for _ in range(10):
#     print("Hello")

#print(end="\t") 옆으로 출력

# for i in range(3):
#     print(i+1,"번")
#     no=i+1
#     name=input("이름 입력: ")
#     kor=int(input("국어 점수: "))
#     print("{}\t{}\t{}".format(no,name,kor))

# for i in range(1,10):
#     print(f"2X{i}={2*i}")
# sum=0
# for i in range(1,101):
#     sum=sum+i
#     print(sum)
# print("합계: :",sum)

# sum 100 넘어가는 시점의 숫자가 몇일까요?
# for i in range(1,101):
#     sum=sum+i
# if sum>11:
#     print("100보다 클 때: ",i-1)
#     print("합계: :",sum)
#     break

# for i in range(2,10):
#     for j in range(1,10):
#     print("{}X{}={}".format(i,j,i*j))

for i in range(0,10):
    for j in range(0,10):
        print((i*10)+j+1,":",j)