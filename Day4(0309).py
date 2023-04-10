#파이썬 3 ppt 연습문제 (p.74)
days = {'January':31, 'February':28, 'March':31, 'April':30,
        'May':31, 'June':30, 'July':31, 'August':31,
        'September':30, 'October':31, 'November':30, 'December':31}
'''
month=input('month:')
print(days[month.title()])

days_key = list(days.keys()) 
print(sorted(days_key))

for x in days:
    if days[x] == 31:
        print(x)
        

days_item = days.items() #튜플로 묶어준다.
print(sorted(days_item))
days_item = [(day,month) for (month,day) in days_item] #키와 벨류값 바꿔주기
days_item.sort()
print(days_item)
days_item = [ (month,day)  for (day,month) in days_item]
print(days_item)

틀린 흔적
values_list = list(days.values())
days_list = sorted(values_list)
items_list = list(days_list.items())
print(items_list)
'''
'''
month = input("month : ")
for x in days:
    if x [0:3] == month.title():
        print(days[x])

#75
d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
   {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
   {'name':'Princess', 'phone':'555-3141', 'email':''},
   {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

for people in d :
    if people['phone'][7]=='8':
        print(people['name'])

for people in d :
    if people['email']=='':
        print(people['name'])
        
s_name = input("name :")
flag = i
for people in d :
    if people['name'] == s_name.title():
        print(people['phone'],people['email'])
        flag = 0
if flag == 1:
    print('없는 사람입니다.')
    
'''
'''
#90
import random
pick = set()
while len(pick)<6:
    pick.add(random.randint(1,45))
print(sorted(pick))
'''
'''
#93
grades = {"Alice": [85, 90, 95],
    "Bob": [75, 80, 85],
    "Charlie": [95, 95, 95]}
for name, grade_list in grades.items():
    print(name,sum(grade_list)/len(grade_list))
'''
'''
#94
num = ([1, 2, 2, 3, 3, 3, 4, 4, 5])
x = set([1, 2, 2, 3, 3, 3, 4, 4, 5])
print("Sum of unique numbers : ", sum(x))
'''
#95
'''
#t = set(Hello, world!)
text = "Hello, world!"
freq_dict = {} #빈도수(frequency)가 딕셔너리 형식으로
for char in text:
    if char not in freq_dict:
        freq_dict[char] = 1
    else:
        freq_dict[char] += 1
print(freq_dict)
'''
'''
#파이썬4 ppt(p.6)
def add_n(n):
    t = 0
    for n in range(1,n+1):
        t += n
    return t

def cir_area(r):
    return 3.14 * r ** 2

def cir_cirm(r):
*    return 2 * 3.14 * r

def den(n):
    cd = []
    for i in range(1,n+1):
        if n%i == 0:
            cd.append(i)
        return cd
print(add_n(50))
print(round(cir_area(3.5),1))
print(round(cir_cirm(3.5),1))
print(den(32))
'''
#17
def box(n,m):
    for i in range(m):
        for j in range(n):
            print('*',end='')
        print(box(2,4))
        
#18
def digit_sum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

