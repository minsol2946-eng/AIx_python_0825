# #딕셔너리-{} 중괄호 사용
# a_dic={"바나나":1,"딸기":3,"사과":2}
# print(a_dic["바나나"]) #출력
# #추가
# a_dic["배"]=5
# print(a_dic)
# #삭제
# del a_dic["바나나"]
# #수정
# a_dic["사과"]=100
# print(a_dic)


# alist=[1,2,3]
# alist=[]
# alist2=alist    #얕은 복사
# # alist2=[*alist] #깊은 복사

# a=["바나나","딸기","사과","딸기","딸기","사과"]
# # print(aa.count("딸기"))
# # a_dic={"바나나":1,"딸기":3,"사과":2}
# aa_dic={}
# for a in a:
#     if a not in aa_dic:
#         aa_dic[a]=1
#     else:
#         aa_dic[a]=aa_dic[a]+1
#         print("있습니다.")


# #리스트 생성 방법
# a1=[1,2,3,4,5]
# a2=[0]*5
# a3=list(range(1,6))
# a4=[i for i in range(1,6) if i%2==0]    #리스트 내포
# print(a4)


# #리스트 묶기
# a = [1,2,3,4,5]
# b = [10,20,30,40,50]
# c = []

#1
# for i in range(len(a)):
#     c.append([a[i],b[i]])
# print(c)

#2
# for i,j in zip(a,b):
#     c.append([i,j])
# print(c)

#3
# c=list(zip(a,b))
# print(c)

# #4
# d=dict(zip(a,b))
# print(d)

# aa = "가나다라가가가나나다라라라라라라라"
# #->{가:10,나:5,다,11}
# a_dic=[]
# for i in aa:
#     if a not in a_dic:
#     a_dic[a]=1
# else:a_dic+=1

# print(a_dic)

# aa="a/b/c/d/e"
# aa_list=list.split("/")
# print(aa_list)

# bb="100,10,5,4,1" #합을 구하시오
# bb_lict=bb.split(",")
# print(bb_list)
# bb_list2=[int(i for i in bb_list)]
# for b in bb_list:
#     sum+=b

# print(bb_list2)
# print("합: ",sum)

# ss="파이썬 공부!! 열심히 합시다.파이썬"
# print(ss.count("공부"))
# print(ss.count("파이썬"))
# print(ss.find("공부"))
# print(ss.find("딸기")) # 없음 -1
# print(ss.index("딸기")) # 없음 error

# ss="   파이썬"
# ss2="<<<<파<<이<<<<썬"

# print(ss.strip())
# print(ss2.replace("<",""))

#join
aa="/"
bb=(aa.join("바나나"))
print(bb)
print(type(bb))














#####선생님

# ss = "   파이썬"       #파이썬 - strip
# ss2 = "<<<<파<<이<썬"  #파이썬 -replace
# print(ss.strip())
# print(ss2.replace("<",""))


# aa = input("이름을 입력하세요.>> ").strip()

# aa = [1,2,   3, 4 ,5]




# ss = "파이썬 공부!! 열심히 합시다. 파이썬"
# print(ss.count("공부"))
# print(ss.count("파이썬"))
# print(ss.find("공부"))  #4
# print(ss.find("자바"))  #없을때 : -1
# print(ss.index("자바")) # index는 없을때 에러




# aa = "a/b/c/d/f/g"
# aa_list = aa.split("/")
# print(aa_list)

# bb = "100,10,5,4,1"
# # 모든수의 합을 구하시오.
# bb_list = bb.split(",")
# bb_list = [int(i) for i in bb_list]
# sum = 0
# for b in bb_list:
#     sum += b
# print(bb_list)
# print("합계 : ",sum)

# bb_list2 = [int(i) for i in bb_list]
# print(bb_list2)




# aa = "가나다라가가가나나다라라라라라라라"
# ##
# # {가:10,나:5,다:11...}
# aa_dict = {}
# for a in aa:
#     if a not in aa_dict:
#         aa_dict[a] = 1
#     else:
#         aa_dict[a] += 1


# print(aa_dict)



# a = [1,2,3,4,5]
# b = [10,20,30,40,50]
# c = []

# c = list(zip(a,b))
# d = dict(zip(a,b))
# print(c)
# print(d)

# for i,j in zip(a,b):
#     c.append([i,j])
# print(c)

# for i in range(len(a)):
#     c.append([a[i],b[i]])
# print(c)




# 리스트 생성방법
# a1 = [1,2,3,4,5]
# a2 = [0]*5
# a3 = list(range(1,6))
# a4 = [i*i+2 for i in range(1,6) if i%2==0] #리스트내포
# print(a4)


# # a = ["바나나","딸기","사과","딸기","딸기","사과"]
# aa = [1,2,3,1,1,1,2,3,1,1,1,2,2,3]
# # print(aa.count("딸기"))
# # {"바나나":1,"딸기":3,"사과":2}
# aa_dic = {}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a] = 1
#     else:
#         aa_dic[a] = aa_dic[a]+1
#         print("있습니다.")

# print(aa_dic)

# 딕셔너리
# a_dic = {"바나나":1,"딸기":3,"사과":2}
# print(a_dic["바나나"])  #출력
# a_dic["배"] = 5         #추가
# print(a_dic)
# del a_dic["바나나"]      #삭제
# print(a_dic)
# a_dic["사과"] = 100      #수정
# print(a_dic)

# a = 10
# a2 = 0
# a2 = a
# print(a2)
# a = 100
# print(a2)


# alist = [1,2,3]
# alist2 = []
# alist2 = alist      # 얕은복사
# # alist2 = [*alist] # 깊은복사
# print(alist2)  # 1,2,3


# alist[0] = 100
# print(alist2)
