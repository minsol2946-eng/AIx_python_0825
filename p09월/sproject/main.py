from p09월.sproject.student import Student
from p09월.sproject.students import Students

# s = Student()
# s.no=1
s1=Student(1,"홍길동",100,100,100)
s2=Student(2,"유관순",100,100,100)
# print(s1.no,s1.name)

st=Students()
st.add(s1)
st.add(s2)

print(st.slist)




# 스튜던트-클래스
# 홍길동 스튜리스트.어팬드()
# 유관군 스튜이스트.어팬드()

# #학생성적을 for문 사용해서 출력.

# from student import Student

# stuList=[]

# s1=Student(1,"강아지",100,50,100)
# s2=Student(2,"고양이",70,90,100)

# stuList.append(s1)
# stuList.append(s2)

# for s in stuList:
#     print(s)