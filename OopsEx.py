# 1111111111111111111111111111111
class Animal:
    name = "Horse"
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def display(self):
        print(self.n, self.a)

    def sound(self, voice):
        print(self.n + " speaks " + voice)


# cat = Animal(Animal.name , 4)
cat = Animal("Tom", 4)
cat.display()
cat.sound("Meow")
# print(cat.sound.voice)
#----------------------------------------------------------------------
# =====================================================================
#22222222222222222222222222222
class SchoolMember:
    def __init__(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.gen = input("Enter Gender : ".upper())

    def description(self):
        print('The School Member details are : \n')
        print("Name : " + self.name)
        print('Age : '+str(self.age))
        print("Gender : "+self.gen)


class Teacher(SchoolMember):
    def __init__(self):
        SchoolMember.__init__(self)
        print("For Teacher")
        self.sub = input("Subject : ")
        self.sal = int(input("Salary : "))

    def description(self):
        SchoolMember.description()
        print("Subject: "+self.sub)
        print("Salary : "+str(self.sal))


class Student(SchoolMember):
    def __init__(self):
        SchoolMember.__init__(self)
        print("For Student")
        self.year = int(input("Enter Year 1/2/3/4:"))
        self.cgpa = int(input("Enter CGPA out of 10 :"))

    def description(self):
        SchoolMember.description(self)
        print("Year: " + str(self.year))
        print("CGPA :" + str(self.cgpa))


t = Teacher()
t.description()
#s = Student()
#s.description()

#-----------------------------------------------------------------------
#====================================================================
#33333333333333333333333333
class SuperChild:
    def __init__(self):
        print('SuperChild initialised')


class UnsuperChild:
    def __init__(self):
        print('UnsuperChild Initialized')


class Child(SuperChild):
    def __init__(self):
        print('Child Initialised')
        SuperChild.__init__(self)


class Demo(UnsuperChild):
    def __init__(self):
        print('Demo Initialised')
        UnsuperChild.__init__(self)


class Foo(Demo, Child):
    def __init__(self):
        print('Foo initialised')
        Demo.__init__(self)
        Child.__init__(self)


f = Foo()
#----------------------------------------------------------------------
#=======================================================================

#4 --Data Hiding/ Abstraction
class MyClass:
    __salary = 100000
    def add_incriment(self, inc):
        self.__salary += inc
        print(self.__salary)

m = MyClass()

m.add_incriment(10000)
m.add_incriment(20000)

#----------------------------
#==================================================================

#5
@staicMethod and @classmethod
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear (cls, name, year):
        return cls(name, date.today().year-year)

    @staticmethod
    def isAdult(age):
        return age > 18


p = Person("Sagar", 25)
p1 = Person.fromBirthYear('sagar', 1992)
print(p.age)
print(p1.age)

print(Person.isAdult(25))
#--------------------------------------------------------------------------------
#================================================================================

#6
class Demo:
    a = 'Python'

    def __init__(self, name, age):
        self.n = name
        self.ag = age

    def display(self):
        print(f'name is {self.n} and age is {self.ag}')
        print(f'Course name is {self.a}')


obj = Demo('Pratik', 22)
obj.display()
obj1 = Demo ('Patil', 22)
obj1.display()

#print(obj1.name)
#print(Demo.name)
print(obj1.a)
print(Demo.a)
#---------------------------------------------------------------------------------------
#=======================================================================================

#7 Instance Variable
class Demo:
    a = 'python'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print(f'Value of instance variable a is {self.a} and b is {self.b}')
        print(f'value of class variable a is {Demo.a}')


obj = Demo(10, 20)
obj.display()

print(Demo.a)
print(obj.a)

#------------------------------------------------------------------------------------------
#==========================================================================================

#8 cumulative Sum
# wap to write cumulative sum of a sequence
L = [11, 3, 4, [9, 2, 3], [5, 6], 11, 8, [1, 2]]


def cum_sum(seq):
    total = 0
    for i in seq:
        if type(i) == list:
            total = total + cum_sum(i)
        else:
            total = total+i

    return total


print(cum_sum(L))
#------------------------------------------------------------------------------------------
#==========================================================================================

#9
#Threading Lock example
import threading, time
tL = threading.Lock()


def timer (name, delay, repeat):
    print("Timer" + name + " started \n")
    tL.acquire()
    print(name + " has acquired Lock \n")
    while repeat > 0:
        time.sleep (delay)
        print(name + ' : '+str(time.ctime(time.time())))

        repeat -= 1
    print(name + ' is releasing lock \n')
    tL.releae()
    print("Timer" + name + " is completed \n ")


t1 = threading.Thread(target=timer, args=("Timer1 ", 1,4))
t2 = threading.Thread(target=timer, args=("timer2", 2, 4))

t1.start()
t2.start()
#------------------------------------------------------------------------------------------
#==========================================================================================

#10
#Thread with argument
import threading, time

def cal_square(args):
    print('Calculating squares \n')
    for i in args:
        time.sleep(1)
        print('square : ', i*i)

def cal_cube(args):
    print('cube \n')
    for i in args:
        time.sleep(1)
        print('cube : ', i ** 3)

L =[11, 3, 4, 5]
t1 = threading.Thread(target = cal_square, args = (L, ))
t2 = threading.Thread(target = cal_cube, args = (L, ))

t1.start()
#t1.run()
t2.start()
#t1.join()
t2.join()

#------------------------------------------------------------------------------------------
#==========================================================================================
#11
#Decorator using Wraps
from functools import wraps

def decorator (f):
    @wraps(f)
    def wrapper (*args, **kwargs ):
        if not can_run:
            return 'this func can not run'

        return f(*args, **kwargs)

    return wrapper
@decorator
def foo():
    return 'THis is fool() fun '

can_run = True
print(foo())

#------------------------------------------------------------------------------------------
#==========================================================================================
#12 Regular Expression
import re

# s = "Cats are smarter than dogs"
# m = re.match(r'Cats' , s)
# print(m)
# m1 = re.match(r'dogs' , s)
# print(m1)

# re.split
s = "Words, words, word."
t = re.split(r'\W+', s)
print(t)
t1 = re.split(r'(\W+)', s)
print(t1)
#----------------------------

s1 = "Oa12b3c9"
sp = re.split(r'[a-f]+', s1)
print(sp)
#-----------------------------

s2 = "Baked Beans And Spam"
sb = re.sub(r'\sAnd\s', ' & ', s2)
print(s2)
print(sb)
#-------------------------------------
s3 = "aeiousdhfgaioejdhfekfjfikfjofjfjuuuu"
se = re.findall(r' [ "aeiou" ]', s3 )
print(se)
#-----------------------------------------
# s = '...words...'
# sp = re.split(r'\W*', s)
# print(sp)

s4 = 'rabcdefgyYhFjkloomnopOeorteeeeet'
# sp = re.findall(r'[aeiouAEIOU]+', s4) # re.I
# print(sp)

f = re.finditer(r'[aeiouAEIOU]+', s4)
for i in f:
    print(i.group(0))
#--------------------------------------------


#------------------------------------------------------------------------------------------
#==========================================================================================
#13
# to track number of objects created 
class Test:
    count = 0 
    def __init__(self):
        Test.count = Test.count+1

    @classmethod
    def getNoOfObjects(cls):
        print('The number of objects created:', cls.count)


t1 = Test()
t2 = Test()
t2 = Test()
Test.getNoOfObjects()



#------------------------------------------------------------------------------------------
#==========================================================================================

#------------------------------------------------------------------------------------------
#==========================================================================================

#------------------------------------------------------------------------------------------
#==========================================================================================
#Task
#Spiral Printing of list
#
# class list:
#     def append
#           extend

          

#           L = List(*args)