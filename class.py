# class object ka blueprint hota h isse code ki complexity reduce hoti h isse code reusable ki permission deta h jab tak object create nahi hota tab tak 
# memory allocate nahi hoti h isme attributes ko outside the class bhi create kar sakte h usko object attribute(instence attribute) bolte h object_name-attribute_name
#ager instence attribute banaya h toh usko jayada prefrence milegi class attribute ki jagh ager koi class ka function koi bhi object nahi le raha or use 
#self na dena ho to use static method mark @staticmethod kar dete h jisse self na lagao toh bhi code without type error ke chalta h class ke inder mai jo bhi function 
# banate h object ki property ke use ke liye toh usme self lkhte h toh self ki jagh kuch bhi namm de sakte h but self se redability acchi hoti h 

"""class relative:
    name = "ut"
    age=21#this is a class attribute
    mobno=9575335089
    salary=10000000

rele=relative()
print(rele.name,rele.age,rele.mobno,rele.salary)"""


"""class emp:
    morning="good"
    language="python"
    salary=50000000
    def getinfo(self):
        print(f"the language is {self.language} and salry is {self.salary}")
    def greet(self):
        print(f"the morning is {self.morning}")

ut=emp()
print(type(ut))"""

"""class emp2:
    lang="python"
    salary=12000000
    def getinfo(self):
        print(f"the language is {self.lang} and the salary is {self.salary}")
    @staticmethod#isse ye define kar dete h ki object ki koi property nahi chahiye
    def greet():
        print(f"good morning bhai")
utkar=emp2()
utkar.getinfo()
utkar.greet()"""

"""class emp3:
    lang="python"
    salary=12000000
    def __init__(self):#jo bhi __ isse chalu hote h unhe dunder method kahte h jo automatically call hote h jaise hi object banega wese  hi ye call ho jayega 
        print("this will automatically call and it is a constructor")
    def getinfo(self):
        print(f"the language is {self.lang} and the salary is {self.salary}")
    @staticmethod#isse ye define kar dete h ki object ki koi property nahi chahiye
    def greet():
        print(f"good morning bhai")
utkar=emp3()
utkar.getinfo()
utkar.greet()"""

class emp4:
    lang="python"
    salary=12000000
    def __init__(self,name ,lang,salary):
        self.name=name
        self.lang=lang
        self.salary=salary
        print("this will automatically call and it is a constructor")
    def getinfo(self):
        print(f"the language is {self.lang} and the salary is {self.salary}")
    @staticmethod#isse ye define kar dete h ki object ki koi property nahi chahiye
    def greet():
        print(f"good morning bhai")
utkar=emp4("utkarsh","java","1800000000")#hum idhar bhi instance attribute de sakte h 
print(utkar.name,utkar.lang,utkar.salary)
utkar.getinfo()
utkar.greet()