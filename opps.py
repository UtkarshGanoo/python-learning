
#inheritence ki help se ek class ki property ko other class ki property mai use kar sakte h isme three type ke inheritence hote h 
# single ,multiple ,multilevel super().-function_name() lagane se parent ka constructor bhi chala sakte h ager outside the instance 
# attribute banya h or uski wajh se class attribute change ho raha h to usse bachne ke liye jaise static method dete the uski jagh class method 
# likhenge @classmethod uske function mai self ki jagh cls likhte h  property decorater hote h jab modification mai mai controll akrna h 
# toh setter and getter ka use karte h @attribute_name-.setter 





"""
#this is example of single inheritence
class employee:
    company="ug technology"
    def show (self,salary):
        self.salary= salary
        print(f"this is ug tech and  salary is {self.salary}")

class programmer(employee):
    
    company ="ganoo tech"
    def __init__(self,salary):
        self.salary= salary
        print(f"this is ganoo tech and slary is {self.salary}")

tech1=employee()
tech1.show(1300000)
tech=programmer(1200000)"""

"""
#this is example of multiple inheritence
class employee:
    company="ug technology"
    def show (self,salary):
        self.salary= salary
        print(f"this is ug tech and  salary is {self.salary}")
        
class coder:
    language ="java"
    def printlanguage(self):
        print(f"both company prefer {self.language} language ")

class programmer(employee,coder):
    company ="ganoo tech"
    def __init__(self,salary):
        self.salary= salary
        print(f"this is ganoo tech and salary is {self.salary} and prefer language is {self.language}")

tech1=employee()
tech=programmer(1200000)
b=coder()
tech.printlanguage
tech.show(1300000)
b.printlanguage()"""

"""
#this example is multilevel inheritence 
class emp:
    company ="UG Tech"


class programmer(emp):
    company ="UG Pharma"


class manager(programmer):
    company="UG automobile"
    
obj= emp()
print(obj.company)

obj1= emp()
print(obj1.company,obj.company)

obj2=manager()
print(obj.company,obj1.company,obj2.company)"""

"""
#this is class method 
class student:
    marks =25
    @classmethod
    def show(cls):
        print(f"the class attribute of marks is {cls.marks} ")

stu=student()
stu.marks = 50 #after using class method this will not change the class attribute value 
stu.show()"""


"""
# this property decorater @property ,@.setter,@.getter 
class student:
    marks =25
    @classmethod
    def show(cls):
        print(f"the class attribute of marks is {cls.marks} ")

    @property
    def name(self):
        return f"{self.stufname}{self.stulname}"
    
    @name.setter
    def name(self,value):
        self.stufname =value.split(" ")[0]  #yaha naam ko split kar rahe h first and last name me 
        self.stulname =value.split(" ")[1]

stu=student()
stu.marks = 50 

stu.name="Utkarsh ganoo"
print(stu.name)

stu.show()"""

#this is operator overloading

class number:
    def __init__(self,n):
        self.n=n

    def __mul__(self,num):
        return self.n*num.n
    def __add__(self,num):
        return self.n+num.n
n=number(1)
m=number(2)

print(n*m)
print(n+m)
            









































