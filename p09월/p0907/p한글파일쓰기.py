import os
#"r":읽기    /"w":쓰기   /"a":이어쓰기

#폴더 확인하기: import os 후
fname=input("저장할 파일 이름을 입력(파일명): ")

if not os. path.exists("common"):
    os.makedirs("common")  #->폴더 생성


with open("common/"+fname,"a",encoding="utf-8")as f:
    while True:
        outStr=input("내용 입력: ")
        if outStr=="":break
        f.write(outStr+"\n")

print("파일 내용이 저장되었습니다.")