# lambda kywords ke use se ek function ko expression mai create karte hai join method mainly string mai use kiye jate hai join ke use string ko ek sath likha
# sakte hai 


# without using lambda function 
"""def sqrt(n):
    return n*n
print(sqrt(5))"""

# with lambda function 
"""squrt=lambda n:n*n
print(squrt(5))

num= lambda a,b:a*b
print(num(5,2)"""

#join join always new string generate karti h isliye use use karne ke liye uske new variable mai store karana padta h 
"""mystring =["utkarsh","uday","jayant","ganoo"]
mystring_join="-".join(mystring)
print(mystring_join)"""

# formate 
"""my="{0}is the best business men{1}".format("utkarsh "," nice")
print(my)"""

# map,filter and reduce 
""" map function ko each element ke sath iterable kar deta hai 
l=[1,2,3,4,5]

sqr=lambda x:x*x
sqrt=map(sqr,l)
print(list(sqrt))"""

# filter conditon ke base element ko filter karta hai 

"""l2=[1,2,3,4,5,6]
def eve(n):
    if (n%2==0):
        return True
    return False
filterd_element=filter(eve,l2)
print(list(filterd_element))"""


# reduce ise functools mai se import karna padta hai iske use list ko single elemnt mai covert kar deta hai 

from functools import reduce
l3=[1,2,3,4,5,6,7,8]
sum=lambda a,b:a*b
red_use=reduce(sum,l3)
print(red_use)