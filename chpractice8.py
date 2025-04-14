"""with open ("myfile.txt") as f:
    name1=f.read().lower()

    print(name1.find("engineer"))"""

"""with open("myfile.txt")as f:
    content=f.read()
if("student"in content):
    print("content avilable")"""

"""import random
def game():
    print("you are playing the game ")
    score=random.randint(1,100)
    with open ("myfile1.txt") as f:
        high_score=f.read()
        if(high_score!=""):
            high_score=int(high_score)
        else:
            high_score=0    
    print(f"your high score is = {score}")
    if(score>50):# if score is greater then 50 so write in file 
        with open("myfile1.txt","w") as f:
            f.write(str(score))
    return score

game()"""


"""def table(n):
    table=""
    for i in range (1,11):
        table+=f"{n} x {i} = {n*i}\n"
    with open (f"tables/year{n}.txt","w") as f:
    # n=int(input("enter the no: "))
    # print(table(n))
        f.write(table)
for i in range (2,10):
    table(i)"""

"""word="donkey"
with open("myfile2.txt","r") as f:
    content=f.read()
    # if ("donkey " in content ):
my=content.replace(word,"####")
with open("myfile2.txt","w") as f:
    f.write(my)"""


"""words=["donkey","dog","animal"]
with open("myfile2.txt")as f:
    content= f.read()
for word in words:
    content =content.replace(word,"$"*len(word))
    with open("myfile2.txt","w") as d:
        d.write(content)"""

"""with open("log.htm") as f:
    content=f.read()
    if("python" in content):
        print("yes it is avilabe ")
    else:
        print("not avilable ")"""
    
"""with open("log.htm") as f:
    line=f.readlines()

lineno = 1
for lines in line:
    if("python" in lines):
        print(f"yes it is avilabe in line no{lineno}")
        break 
    lineno += 1
else:
    print("not avilable ")"""


"""with open ("this.txt")as f:
    content=f.read()

with open("this2.txt","w")as d:
    d.write(content)"""

"""with open ("this.txt")as f:
    content1=f.read()

with open ("this2.txt")as f:
    content2=f.read()

if(content1==content2):
    print("yes this file are identicle ")
else:
    print("not identicle ")"""


with open("this2.txt","w")as f:
    f.write("")