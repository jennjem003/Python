# f-string을 이용한 문자열 포매팅
name = "John"
age = 30
height = 175.5

print(f"My name is {name}, I'm {age} years old, and my height is {height:.1f}.")
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

#1번
name = "Tom"
age = 20
print(f"My name is {name},I am {age} years old.")

#2
a = 3
b = 2
c = 1
print (f"I have {a} apple,{b} oranges, and {c} banana")

#3 The result is 1.23.
result = 1.23
print("The result is %.2f"%result)

#4 Your score is 90%.
score = 90
print(f"Your score is {score}%.")

#5 10 + 20 = 30
a = 10
b = 20
c = 30
print(f"{a}+{b} ={c:5d}")
'''
num1 = int(input("사과 개수 : "))
num2 = int(input("사과 가격 : "))
result = num1 * num2
result2 = result * 0.1
#print(f"부과세율 : {result2}")
num3 = int(input("부과세율 : "))
totalresult = num3 + result
print(f"총 가격 : {totalresult}")
'''


#추가문제
#1
'''
sec = int(input("초 입력 : "))
result = sec / 60
result2 = sec % 60
print(f"{result}")
print(f"{result2}")
print(f"{result:.0f}분 {result2:.0f}초")
'''

#2
'''
min = int(input("분 입력 : "))
day = min // 1440
print(f"{day}")
hour = (min%(24*60)//60)
print(f"{hour}")
Min = min % 60
print(f"{Min}")
print(f"{day}일 {hour}시 {Min}분")
'''
#3
principal = 5000000
interestRate = 0.05
year=5
totalAmount = principal*(1 + interestRate )**year
print(f"5년후의 원리금 총액은 {totalAmount:.0f}입니다.")

#4
