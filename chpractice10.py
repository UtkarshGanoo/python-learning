"""class twodvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")

class threedvector(twodvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

a=twodvector(1, 2)
a.show ()
b=threedvector(1,2,3)
b.show ()"""

"""class animal:
    pass

class pets(animal):
    pass 

class dog(pets):
    def __init__(self,sounds):
        self.sounds=sounds
        print(f"the dog is doing {self.sounds}")

d=dog("bow bow")"""


"""class employee:
    salary=1500000
    increment=10%
    
emp=employee()

print(emp.salary,emp.increment)"""


"""class employee2:
    salary=1500000
    increment=10
    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary *(self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.myincrement=((salary/self.salary) -1)*100
    
emp=employee2()
print(emp.salaryafterincrement)
emp.salaryafterincrement=1650000.0
print(emp.myincrement)"""

"""class complex:
    def __init__(self,i,r):
        self.i=i
        self.r=r
    def __add__(self,c2):
        return complex(self.r +c2.r,self.i+c2.i)
    
    def __mul__(self,c2):
        real_part= self.r * c2.r + self.i * c2.i
        img__part= self.r * c2.i + self.i * c2.r
        return complex(real_part,img__part)

    def __str__(self):
        return f"{self.r} + {self.i}i"
c1=complex(1,2)
c2=complex(3,4) 
print(c1+c2)
print(c1*c2)"""

