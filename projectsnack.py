"""here we create a game for snack,water,gun in this  we use mathematical expression for playing game in this we 
use ( (1 for snake) and (-1 for water) and (0 for gun) )

"""
"""import random
youch=input("Enter Your Choice: ").lower()

youdict={"snake":1 , "water":-1 , "gun":0}

computer=random.choice(list(youdict.keys()))

you = youdict.get(youch)
computer  = youdict.get(computer)

if(computer ==-1 and you==1):
    print("😍 you win!")

elif(computer ==1 and you==0):
    print("😍 you win!")
elif(computer ==0 and you==-1):
    print("😍 you win!")

elif(computer ==-1 and you==0):
    print("😫 you loss!")

elif(computer ==0 and you==1):
    print("😫 you loss!")

elif(computer ==1 and you==-1):
    print("😫 you loss!")

elif(computer  == you):
    print("😒 game tie !")

print(f"computer choose {computer} and you choose {youch}")"""


import random
youch=input("Enter Your Choice: ").lower()

youdict={"snake":1 , "water":-1 , "gun":0}

computer=random.choice([-1,0,1])

you = youdict[youch]

if(computer ==-1 and you==1):
    print("😍 you win!")

elif(computer ==1 and you==0):
    print("😍 you win!")
elif(computer ==0 and you==-1):
    print("😍 you win!")

elif(computer ==-1 and you==0):
    print("😫 you loss!")

elif(computer ==0 and you==1):
    print("😫 you loss!")

elif(computer ==1 and you==-1):
    print("😫 you loss!")

elif(computer  == you):
    print("😒 game tie !")

print(f"computer choose {computer} and you choose {youch}")






















































