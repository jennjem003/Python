'''
string = "abcdefghij"

result = ""
for i in range(len(string)):
    if i % 2 == 1:
        result += string[i]

print(result)  # 출력값: "acegi"


s = "Hello, world!"
reversed_s = s[::-1]
print(reversed_s)
# 문자열 대소문자 변환 함수 예시
print("hello, world!".upper())  # "HELLO, WORLD!"
print("HeLLo, wOrLd!".lower())  # "hello, world!"
print("hello, world!".capitalize())  # "Hello, world!"
print("hello, world!".title())  # "Hello, World!"
print("Hello, World!".swapcase())  # "hELLO, wORLD!"

# 문자열 정렬, 채우기 함수 예시
s = "hello"

print(s.center(10))  # "  hello   "
print(s.center(10, "-"))  # "--hello---"
print(s.ljust(10))  # "hello     "
print(s.ljust(10, "*"))  # "hello*****"
print(s.rjust(10))  # "     hello"
print(s.rjust(10, "+"))  # "+++++hello"
print("123".zfill(5))  # "00123"


#파이썬3.ppt 연습문제(27쪽)
print(len(str))
#

#
str[0]
#
print(str[:3])
#
print(str[-3:])
#
reversed_str = str[::-1]
print(reversed_str)
#
if len(str) >= 7:
    print(str[6])
else:
    print("문자가 없습니다.")
#
print(str[1:-1])
#
print(str.upper())
#
print(str.lower())
#
print(str.replace('a','e'))
'''
'''
#파이썬3.ppt 연습문제(28쪽)
#내가 푼거
#a = input('a')
string = input("Your Word:")
string_index = string.index("a")
print(string[:string_index+1])
print(string[string_index+1:])
#정답
string = input("Your Word:")
index_a = word.find('a')
if index_a! = -1:
    print(word[:index_a+1])
    print(word[index_a+1:])
else:
    print(word)
#또는(중복된 a를 하기위한)
print(string.replace('a','a\n'))
'''
'''
#
total = 0
for num in range(1,1001):
    #각 자리 수 합 구함
    digits_sum = 0
    for digit in str(num):
        digits_sum += int(digit)
    #전체 합에 더함
    total += digits_sum
print(total)
sum=0
for s in '234':
    sum += int(s)
'''
'''
words = ['apple', 'banana', 'cherry', 'durian']
word_lengths = [len(word) for word in words]
print(word_lengths)  # [5, 6, 6, 6]
'''
'''
words = ["apple", "banana", "orange", "grape", "watermelon"]
result = [word.upper() for word in words if len(word) >= 6]
print(result)  # ['BANANA', 'ORANGE', 'WATERMELON']
'''
'''
original_list = [[1, 2], [3, 4], [5, 6]]
new_list = [num for sublist in original_list for num in sublist]
print(new_list)  # [1, 2, 3, 4, 5, 6]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [num for row in matrix for num in row if num % 2 == 0]
print(result)  # [2, 4, 6, 8]
'''
#p53
'''
list=['친구1','친구2','친구3']
list.insert(0,'새친구')
print(list)

list.insert(2,'새친구2')
print(list)

list.append('새친구3')
print(list)
'''
'''
#
list=[1,2,3]

list[1]=17
print(list)
#list.insert(4,5,6)
#list1=[4,5,6]
#list2=list+list1
#print(list2)
list += [4,5,6]
print(list)

#list.remove(0)
del list[0]
print(list)

list.sort()
print(list)

list.insert(3,25)
print(list)
'''
#
list = []
for i in range(0,50):
    list.append(i)
print(list)

list2 = []
for j in range(1,51):
    list2.append(j**2)
print(list2)

#
l=[1,2,3]
m=[4,5,6]
lm=[]
for i in range(0,len(l)):
    lm.append(l[i]+m[i])
print(lm)

#몰랐어
list=input("숫자 5개(구분자:띄어쓰기):").split()
result = "+".join(list)
print(result)




