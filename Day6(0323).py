#파이썬7ppt 연습문제 (p18)
'''
data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}

while True:
    try:
        user_input = input("Enter a day of the week")
        value = data[user_input]
        print(value)
    except KeyError:
        print("항목이 없습니다")
        break
'''
'''  
#try-except 안쓴거
data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}

while True:
        user_input = input("Enter a day of the week")
        value = data.get(user_input,None)
        if value is not None:
            print(value)
            break
        else:
            print("항목이 없습니다.")
'''
'''
file = open("example.txt", "w")

# 파일에 문자열을 씁니다.
file.write("Hello, world!\n")
file.write("This is an example file.\n")

# 파일에 문자열의 리스트를 씁니다.
lines = ["We will use it to demonstrate file writing in Python.\n",
         "We can write multiple lines at once.\n"]
file.writelines(lines)

file.close()  # 파일을 닫습니다.
'''
import re

def extract_email(string):
    pattern = r'\b[가-힣A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, string)
    return emails


string = "Jaehwa's email is 가나다라마바사아자차카타파하jenal95@daum.net. Jane can be reached at jane@example.co.uk."

emails = extract_email(string)
print(emails)  # ['john.doe123@example.com', 'jane@example.co.uk']


