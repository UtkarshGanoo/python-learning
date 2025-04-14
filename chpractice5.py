"""a1=int(input("enter the  no: "))
a2=int(input("enter the  no: "))
a3=int(input("enter the  no: "))
a4=int(input("enter the  no: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greater",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greater",a2)
elif(a3>a2 and a3>a1 and a3>a4):
    print("a3 is greater",a3)
elif(a4>a2 and a4>a1 and a4>a3):
    print("a4 is greater",a4)

else:
    print("no one is greater then another")"""

"""a1=int(input("enter the  no: "))
a2=int(input("enter the  no: "))
a3=int(input("enter the  no: "))

total_marks=((100)*(a1+a2+a3))
total_marks=total_marks/300
if(total_marks>=40 and a1>=33 and a2>=33 and a3>=33):
    print("you are pass",total_marks)

else:
    print("you are fail",total_marks)"""


"""c1="click on link"
c2="send massage"
c3="touch to the link"
c4="click here"

massage=input("enter the comment: ")

if((c1 in massage) or (c2 in massage) or (c3 in massage) or (c4 in massage)):
    print("spam comment dont touch it ")


else:
    print("valid comment")"""


"""username=input("enter the user name: ")
if(len(username)<10):
    print("username must contain 10 charecter")

else:
    print("valid user!")"""

"""list=["utkarsh","aakash","nir","rituraj","kanishka"]
name=input("enter the name: ")

if(name in list):
    print("name is in list")

else:
    print("name is not in list")"""

"""marks=int(input("enter the marks: "))
if(marks ==100 and marks >=90):
    grade="EX"

elif(marks <90 and marks >=80):
    grade="A"

elif(marks <80 and marks >=70):
    grade="B"

elif(marks <70 and marks >=60):
    grade="C"

elif(marks <60 and marks >=50):
    grade="D"

elif(marks <50):
    grade="F"

print(grade)"""

post=input("enter the post: ")

if("utkarsh" in post.lower()):
    print("post is talking about the great men")

else:
    print("this post not avilable")
