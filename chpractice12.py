"""name =input("enter the name: ")
marks =int(input("enter the marks: "))
phoneno=int(input("enter the phoneno: "))

dataset1="The Name of student {0} ,marks is {1} and his phone no is {2}".format(name,marks,phoneno)
print(dataset1)"""

"""L1=[65,1,5,32,5,2,25,5,2,102,1,4,5,1,4]
DIV_5=lambda a:a%5==0
final_div=list(filter(DIV_5,L1))
print(final_div)"""

from functools import reduce 
L1=[65,1,5,32,5,2,25,5,2,102,1,4,5,1,4]

def maxi(a,b):
    if (a>b):
        return a
    return b
print(reduce(maxi,L1))
