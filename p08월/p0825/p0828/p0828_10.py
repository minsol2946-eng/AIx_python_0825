#Q.반복문을 사용해서 1-100까지 합을 출력하세요
total=0
for i in range(1,101):
    total+=i
print(total)

#200을 넘는 때의 i의 값과 i번째 합계를 출력.
total = 0

for i in range(1, 101):
    total=total+i
    if total>200:
        print(f"i: {i}, total: {total}")
        break
print(total)

#200을 넘는 이전 시점의 i, 합계를 출력.
total = 0

for i in range(1, 101):
    if total + i > 200:
        print(f"i: {i - 1}, total: {total}")
        break
    total=total+i
print(total)

#구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()