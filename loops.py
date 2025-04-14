#to done the repetative work in very less complex 


#while loop -->python mai while loop ka syntax ' while (condition): ' is trah hota other language ke behalf mai

"""i=1
while i<=50:
    print(i)
    i+=1"""

"""list=[1,2,5,6,8,9]
i=0
while(i<len(list)):
    print(list[i])
    i+=1"""
print("------------------------for loop------------------------------")

#iska use list tuple string ko iterate karne ke liye hota hai isme ek range naam ka function hota hai jisse (kahase,kahatak kitne skip) karke
#but 'kitne skip' ye batana jaruri nahi hota hai 

"""mylist=[1,2,5,6,8] 
for i in mylist:
    print(i)
    i+=1

tup=(1,8,9,3,4,6,5,8,525,6,8)
for i in range(0,len(tup)):
    print(tup[i])

string = "utkarsh"
for i in string:
    print(i)

for i in range(0,15):
    print(i )"""

'''l=[5,6,8,5,4,8,56,6]

for item in l:
    print(item)
else:
    print("item not found")'''


print("--------break---------------continue---------------------pass------------------------")

#break --> jaise hi if ki condition hit hogi uske baad kuch print nai hoga 
for i in range(10):
    if(i==4):
        print("i is greater then four ")
        break
    print(i)

#continue --> kisi value ko ager skip karna ho toh continue ka use karte hai 
for i in range (50):
    if(i==45):
        continue
    print(i)

#pass --> ager kisi 2 loop ki execute karna chahte hai or 1st loop ki jagh secound loop ka ouput ddekhna chhte h toh 1st loop mai pass likh denge

for i in range(20):
    pass

while(i<20):
    print(i)
    i+=1


