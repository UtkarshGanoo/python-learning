"""def findgreatest(a,b,c):
    if(a>b and a>c):
        print(f"a is greater {a}",)
    elif(b>a and b>c):
        print(f"b is greater {b}")

    elif(c>a and c>b):
        print(f" c is greater {c}")
    
    return "equal "

a=int(input("enter the no "))
b=int(input("enter the no "))
c=int(input("enter the no "))
findgreatest(a,b,c)"""

"""def cel_to_fer(cel):
    return (cel*9/5)+32

cel=float(input("Enter the temprature in celcius: "))
print(cel_to_fer(cel))"""

"""def fer_to_cel(fer):
    return (fer-32)*5/9

feren=float(input("enter the temperature in ferehite: "))
temp=fer_to_cel(feren)
print(round(temp,2),"°F")"""

"""def natural_no_sum(n):
    if(n==1):
        return 1
    return natural_no_sum(n-1) + n

n=int(input("enter the no: "))
print(natural_no_sum(n))"""


"""def inch_to_cm(inch):
    return inch*2.54

print(inch_to_cm(10.0))"""

def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {i*n}")
table(2)