#파이썬 ppt5
'''
class Calculator:
    # 클래스 변수
    operator = '+'

    # 클래스 메서드
    @classmethod
    def set_operator(cls, new_operator):
        cls.operator = new_operator

    # 인스턴스 메서드
    def calculate(self, num1, num2):
        if Calculator.operator == '+':
            return num1 + num2
        elif Calculator.operator == '-':
            return num1 - num2
        elif Calculator.operator == '*':
            return num1 * num2
        elif Calculator.operator == '/':
            return num1 / num2
# 파이썬 ppt5 (p.21)
#Deposit 클래스를 생성하라.
#이 클래스는 세 개의 인스턴스 변수 initial과 interest, n을 갖는다.
#initial은 원금을 의미하고 interest는 년 이자율을 나타낸다.
#초기화 함수에서 세 개의 인스턴스 변수를 전달 받은 값으로 설정해야 한다.
#클래스 메소드 profit()은 n년 후 원리금을 반환한다.
#n년 후 원리금은 initial * (1 + interest)n이다.
#Deposit 클래스를 이용하여 100만원을 이율 3.5%로 7년간 저축했을 때 원리금을 구하는 프로그램을 작성하라. 단 원리금은 정수로 표시되어야 한다.
class Deposit:
    def _init_(self,initial,interest,n):
        self.initial = initial
        self.interest = interest
        self.n = n
    def profit(self):
        return int(self.initial*(1+self.interest)**self.n)
x = Deposit(1000000,0.035,7)
print(x.profit())
'''
'''
#예제의 Teacher 클래스에서 People 클래스의 __init__()를 호출하지 않고
#부모 클래스의 age, name 인스턴스 변수를 이용할 수 있는가?
#이용할 수 없다면 그 이유는? 이용할 수 있게 하려면 프로그램을 어떻게 수정해야 하는가?
class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))
        
    def get_age(self):
        return self.__age
        
    def set_age(self,age):
        self.__age=age
        
    def get_name(self):
        return self.__name
        
    def set_name(self,name):
        self.__name = name

class Teacher(People) :
    def __init__(self, age=0, name=None, school=None) :
        super().__init__(age, name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)
t = Teacher(35,"kim","pnu")
t.introMe()
t.set_name('lee')
t.introMe()
t.showSchool()

#
class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def getName(self): 
        print(self.name) 

    def getAge(self): 
        print(self.age) 

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name,age)
        self.employeeID = employeeID
        
    def getID(self):
        return self.employeeID
emp = Employee('동양',65,2019)
print(f'ID:{emp.getID()}')
'''

'''
class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
    
    def attack(self):
        print(f"{self.name} attacks with a normal attack.")

class Warrior(Character):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health)
        self.strength = strength
    
    def attack(self):
        print(f"{self.name} attacks with a mighty swing.")
    
    def smash(self):
        print(f"{self.name} smashes the ground with a powerful blow.")

class Mage(Character):
    def __init__(self, name, level, health, magic):
        super().__init__(name, level, health)
        self.magic = magic
    
    def attack(self):
        print(f"{self.name} casts a magic missile.")
    
    def teleport(self):
        print(f"{self.name} teleports to a nearby location.")


c = Character("Bob", 10, 100)
c.attack()  # Bob attacks with a normal attack.

w = Warrior("Conan", 20, 200, 15)
w.attack()  # Conan attacks with a mighty swing.
w.smash()   # Conan smashes the ground with a powerful blow.

m = Mage("Merlin", 15, 150, 30)
m.attack()  # Merlin casts a magic missile.
m.teleport()  # Merlin teleports to a nearby location.
'''
# p.49
class Student:
    def __init__(self, name, studentID, year, major, avg_score):
        self.name = name
        self.studentID = studentID
        self.year = year
        self.major = major
        self.avg_score = avg_score
    def get_info(self):
        return  f"이름:{self.name}, 학번:{self.studentID}, 학년:{self.year},
                    전공:{self.major}, 평균성적:{self.avg_score}"

class StudentManager
    def __init__(self):
        self.student_list = []
    def add_student(self,student):
        self.student_list.append(student)
    def show_all_students(self):
        for student in self.student_list:
            print(student.get_info())
    def remove_student(self,studentID):
        for student in self.student_list:
            if student.studentID == studentID:
                self.student_list.remove(student)
                return
        print(f'{student_id}학번을 가진 학생이 없습니다.')
    def find_student(self,studentID):
        for student in self.student_list:
            if student.studentID == studentID:
                print(f'{studentID}는 {student,name} 학생입니다.')
                return
        
student_mamager = StudentManager()

student1 = Student('홍길동', '20230001', 2, '컴퓨터공학', 90.5)
student2 = Student('김철수', '20230002', 4, '전자공학', 82.5)
student3 = Student('이영희', '20230003', 1, '건축공학', 92.5)

student_mamager.add_student(student1)
student_mamager.add_student(student2)
student_mamager.add_student(student3)

student_mamager.show_all_student()