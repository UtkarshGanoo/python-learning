# in the python the function creation starts from "def function_name()" like this and whenever you need that function you can use function doing function call
#funtion is a block of code in that we can saparate the logic we can call function like this "function_name()" there are two type of function 1st built in function and
#2nd user define function ager argument mai fix kar di ha koi si string tho or calling ke time koi si alg string denge toh woh alg wali string chalegi wrna 
# default wali chalegi 
"""def average():

    a=int(input("enter the no: "))
    b=int(input("enter the no: "))
    c=int(input("enter the no: "))
    avg=int((a+b+c)/3)
    print(avg)

average()"""

"""print("utkarsh ", end="")
def greet():
    print("good day")
greet()"""


'''def good(name, end):
    print("good day and you are the best."+name)
    print(end)
    return "function executed !"
a=good("utkarsh","welcome")
print(a)'''


"""def good1(name, end="dhanyawad"):
    print("good day and you are the best."+name)
    print(end)
    return "function executed !"

b=good1("utkarsh","welcome")#the welcome is return
c=good1("utkarsh")#the by defalut value will return 
print(b)
print(c)"""

print("-----------------------------------recursion--------------------------------------")
#a function can call itself it is called as recursion 
def factorial(n):
    if(n==0 or n==1) :
        return 1
    return n*factorial(n-1)

n=int(input("enter the no: "))
print(f"the factorial of n is {factorial(n)}")


