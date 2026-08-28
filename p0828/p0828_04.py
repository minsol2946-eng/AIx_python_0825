
#문자열 함수
#strip, splite, replace, fide, rfind
#upper:대문자, lower:소문자

paper="""네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 
2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다.
이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서
비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."""

print(paper)
print(len(paper))

#split 특정 문자를 기준으로 분리를 해줌
str1="1,홍길동,100,100,100,300,100"
s=str1.split(",")
print(s)
print(s[2])

str2="2026-08-28"
s2=str2.split("-")
print(str2)
print(s2)

str4="EDMS,307-2E-PS-W-611-W008,VF5770"
s4=str4.split(",")
print(s4)
print(s4[1])

#strip: 공백 제거
aaa1="     안녕하세요     "
print(aaa1)
print(aaa1.strip())

aaa2="   안녕   하세요  ."
print(aaa2)
print(aaa2.strip()) #글자 사이 공백은 제거 안됨

#replace-문자를 설정 문자로 대체
aaa3="kkggyy"
aaa5=aaa3.replace("gg","ㅋㅋ")
print(aaa5)

#find: 검색 함수 있으면 위치를 반환, 없으면 -1
aaa6="동해물과백두산이"
print(aaa6.find("백두"))
#rfind: 오른쪽에서부터의 순서로 위치를 검색


#upper:대문자, lower:소문자
r="hello"
print(r.upper())