#파일 복사하기
import os

# rf=open("c:/aaa/1.jpg","rb")
# wf=open("c:/aaa2/2.jpg","wb")

# while True:
#     fdata=rf.read(1)
#     if not fdata:break
#     wf.write(fdata)

# rf.close()
# wf.close()
# print("이미지 파일이 복사 되었습니다.")

readF=open("c:/aaa/siss.jpg","rb")
writeF=open("c:/aaa2/siss2.jpg","rb")
while True:
    Jdata=readF.read(1)
    if not Jdata:break
    writeF.write(Jdata)

readF.close()
writeF.close()
print("복사 완료")