class Students:
    slist=[]

    def add(self,s):
        self.slist.append(s)

    def print(self):

stus=Students()

s1=(Students(1,"강아지",100,50,100))
s2=(Students(2,"고양이",70,90,100))

stus.add(s1)
stus.add(s2)