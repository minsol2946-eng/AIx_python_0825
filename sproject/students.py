class Students:
    slist=[]

    def add(self,s):
        self.slist.append(s)

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.1f}"


