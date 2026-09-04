##########람다식##########
# #ex
# def sum(n1,n2):
#     result=n1+n2
#     return result
# print(sum(10,20))

#함수 요약
#명령어 1줄만 가능
# sum=lambda n1,n2:n1+n2
# print(sum(10,20))

# sum=lambda n1:n1+10
# print(sum(10))

####map#####
#map(함수,리스트)
# mlist=[5,15,25,35]
# a_arr=[m+10 for m in mlist] #리스트내포
# print(a_arr)

# data=["100","200","300"] #문자열
# result=map(int,data) #맵사용 정수 변경
# print(list(result)) #출력시 리스트로 변경 출력

# #
# a=[1,2,3]
# b=[10,20,30]
# result=map(lambda x,y:x+y, a,b) #a->x / b->y
# print(list(result))




########재귀함수 fatorial########
#자기자신의 함수를 다시 호출
###1-4까지 곱을 구하시고
for i in range(1,5):
    result *=i
print(result)


def fact1(num):
    if num<=1:
        return num
    else: return num*fact1(num-1)
print(fact1(4))