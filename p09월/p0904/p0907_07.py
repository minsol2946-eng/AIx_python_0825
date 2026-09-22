#####파일 쓰기####
with open("c:/aaa/abc.txt","a",encoding="utf-8") as f:  #a:이어쓰기/w:덮어쓰기/r:읽어오기
    while True:
        line=input("글을 입력하세요>>> ")
        if line !="":
            f.writelines(line+"\n")
        else:
            break

print("파일이 저장되었습니다.")