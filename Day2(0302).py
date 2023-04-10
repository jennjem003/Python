'''
num = 10
result = "10보다 큽니다" if num > 10 else "10보다 작거나 같습니다"
print(result)

score = int(input("성적을 입력하세요: "))
grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))
print(grade)

score = int(input("성적을 입력하세요: "))
grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))
print(grade)

Ascore = int(input("국어 성적을 입력하세요: "))
Bscore = int(input("영어 성적을 입력하세요: "))
Cscore = int(input("수학 성적을 입력하세요: "))
int(f"각 과목의 평균 점수 : {Ascore} , {Bscore} , {Cscore}")
avgscore = ({Ascore}+{Bscore}+{Cscore})/3
grade = "A" if avgscore >= 90 else ("B" if avgscore >= 80 else ("C" if avgscore >= 70 else ("D" if avgscore >= 60 else "F")))
print("학점 : ",{grade})
'''
'''
num = int(input("숫자를 입력하세요: "))
sign = "양수" if num > 0 else ("음수" if num < 0 else "0")
print(sign)'''
'''
cm = int(input("길이 입력 :"))
sign = "({cm}%2.54)인치" if cm > 0 else ("잘못입력하였습니다." if cm < 0 else "0")
print(sign)'''

'''
grade = int(input("학점 입력 : "))
if grade<40:
    print("1학년 입니다.")
elif 40<=grade<80:
    print("2학년 입니다.")
elif grade>=80:
    print("졸업반 입니다.")'''
'''
time = int(input("Enter Hour : "))
apm = int(input("am(1) or pm(2) : "))

overtime = int(input("how many hours ahead : "))
newtime = time + (overtime%24)

if newtime>12:
    if apm == 1:
        apm = "pm"
    else:
        apm = "am"
    print("new hour : %d %s"%(newtime % 12, apm))
else:
    if apm ==1:
        apm="am"
    else:
        apm = "pm"
    print("new hour : %d %s"%(newtime, apm))
'''
text = "Python"
'''
for char in text:
    print(char)
    
for i in range(5):
    print(i)
    

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="")
    print()

for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("*", end="")
    print()
'''
'''
n = int(input("양의 정수 n을 입력하세요 : "))
sum=0
for i in range(1,n+1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i 
print("1부터 10까지의 자연수 중에서 3의 배수와 5의 배수의 합 : ",sum)
'''
'''
a = int(input("1번째 숫자를 입력하세요 : "))
b = int(input("2번째 숫자를 입력하세요 : "))
c = int(input("3번째 숫자를 입력하세요 : "))
d = int(input("4번째 숫자를 입력하세요 : "))
e = int(input("5번째 숫자를 입력하세요 : "))

numbers=[a,b,c,d,e]
max_number = max(numbers)
min_number = min(numbers)

print("최댓값 :",max_number,"최솟값 : ",min_number)


#또는 교수님 정답
max_num = 0
min_num = 100

for i in range(5):
    num = int(input(f"[최댓값과 최솟값 찾기]\n\n{i+1}번째 숫자를 입력하세요:"))
    
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num=num
output = f"\n[결과]\n입력받은 숫자들 :
{[max_num,min_num]}\n최댓값: {max_num}\n최솟값 : {min_num}"
print(output)
'''
'''
sum=0
while sum <100:
    num = int(input(f"[숫자의 합이 100보다 작을 때까지 입력받기]\n\n숫자를 입력하세요:"))
    sum += num
output = f"\n[결과]\n입력받은 숫자들의 합 : {sum}"
print(output)
'''
'''
num = int(input("몇 번째 항을 출력할까요? (1 이상의 양의 정수) : "))
for i in range(2,n)
    i-2
'''
'''
num = int(input("몇 번째 항을 출력할까요? (1 이상의 양의 정수) : "))

a, b = 1, 1
for _ in range(n):
    a, b = b, a + b
    return a

result = num(n)
print("피보나치 수열의", n, "번째 항은", result, "입니다.")
'''
'''
n=int(input("[피보나치 수열의]\n\n몇번째 항을 출력할까요 (1 이상의 양의 정수) : "))

if n == 1 or n == 2:
    result=1
else:
    a,b=1,1
    i = 3
    while i <=n:
        result = a+b
        a=b
        b=result
        i += 1
output = f"피보나치 수열의 {n}번째 항은 {result}입니다."
print(output)
'''
'''
import random

# 1부터 100 사이의 임의의 수를 선택합니다
secret_number = random.randint(1, 100)

while True:
    # 사용자가 숫자를 입력합니다
    guess = int(input("Guess the secret number (between 1 and 100): "))

    # 입력한 숫자와 비교합니다
    if guess < secret_number:
        print("Up")
    elif guess > secret_number:
        print("Down")
    else:
        print("Correct!")
        break  # 정답을 맞췄으므로 반복문을 종료합니다
        
'''
'''
import random

dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
random_number = random.sample(dice1,1)
random_number2 = random.sample(dice2,1)
if random_number + random_number2 =7
'''
'''    
import random

while True:
    dice1 = random_randint(1,6)
    dice2 = random_randint(1,6)
    dice_sum = dice1 +dice2
    print(f"주사위 1 : {dice1},주사위2 : {dice2}, 합 : {dice_sum}")
    if dice_sum ==7:
        print("이겼습니다!")
    else:
        print("다시 던집니다.")
'''
'''
from random import randint

money = 50
target_money = 100

while money> 0 and money < target_money:
    guess = int(input("앞면(1) 또는 뒷면(2)을 맞춰보세요: "))  # 플레이어의 예상
    coin = randint(1,2) #1 또는 2를 임의로 발생
    if guess == coin:  # 맞췄을 경우
        money += 9
        print("맞추셨습니다! 현재 자금:", money)
    else:  # 틀렸을 경우
        money -= 10
        print("틀리셨습니다. 현재 자금:", money)
# 게임 종료 후 결과 출력
if money <= 0:
    print("패배! 모든 자금을 잃었습니다.")
else:
    print("승리! 목표 자금", target_money, "을 달성했습니다.")

from random import randint
p=50
while true:
    coin= randint(1,2)
    guess= int(input("Your Guess : "))
    if not ((guess == 1) or (guess ==2)):
        print(guess,"Try again")
        continue
    if coin == guess:
        p = p + 9
        print("You Win!, Your total : ",p)
    else:
        p = p - 10
        print("You loss!, Your total : ",p)
'''    
int(input("숫자를 입력하시오 : "))
for i in range(min(a,b),0,-1):
    if a%i == 0 and b%i == 0:
        print(i)
        break
    
    
num_1 = int(input('number 1 : '))
num_2 = int(input('number 2 : '))
if num_1 > num_2:
    max_num= num_1
    min_num= num_2
else:
    max_num= num_2
    min_num= num_1
rem = 1
while rem !=0:
    max_num=min_num
    min_num= rem
print("최대공약수는",max_num,"입니다.")