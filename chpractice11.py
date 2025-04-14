"""try:
    with  open ("my1file.txt")as f1:
       content1=f1.read()
       
except Exception as e:
    print(e)   
try:
    with  open ("myfile2.txt")as f2:
       content2=f2.read()
       print(content2)
       
except Exception as e:
    print(e)   
try:
    with  open ("my3file.txt")as f3:
       content3=f3.read()
       
except Exception as e:
    print(e)    
print("Thank You ")"""

"""my_list=[1,2,3,4,5,6,7,8]
for i,item in enumerate(my_list):
    if i==2 or i==4 or i==6 :
        print(item)"""

"""num=int(input("Enter A Number: "))

table=[num*i for i in range(1,11)]
print(table)"""

"""try:
    num1=int(input("Enter A Number: "))
    num2=int(input("Enter A Number: "))
    result=num1/num2
    print(result)
    if num2==0:
        print ("not dividing by zero")
except ZeroDivisionError as e:
    print("infinite")"""


num=int(input("Enter A Number: "))

table=[num*i for i in range(1,11)]
print(table)

with open("table.txt","w")as wr:
    wr.write(str(table) + "\n")































































































































