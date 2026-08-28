#Q1. inch단위를 입력받아,cm단위로 바꾸세요.
inch_size=int(input("사이즈 입력: "))
cm_size=inch_size*2.54

print("인치: ",inch_size)
print("센치: ",cm_size)

#Q2.원의 반지름을 입력받아 원의 둘레와 없이를 구하세요.
length=float(input("반지름 입력: "))
pi=3.14
result=pi*(length**2)
print("넓이: ", pi*length*length)
print("넓이: ", pi*length**2)
print("둘레: ",2*pi*length)