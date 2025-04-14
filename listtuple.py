#list like array but not an array it similar storing same data it can stor any data type list are mutable it can be change list can be create using
# '[ ]' this . 
mylist=["bus","car","cycle","bmw","mrcedes","audi"]
print(mylist[3])
print(mylist[4])
print(mylist[5])

mylist[5]="skoda"
print(mylist)

print(mylist[0:6])

# -------------------------------------------------------------------------------
#methods on list 
mylist.append("audi")# add the element in the last of the list 
print(mylist)

list=[2,3,4,5,6,8,9,7,]
list.sort()#sort the list in increasing order
print(list)
list.reverse()#reverse the list in decresing order
print(list)

list.sort()
list.insert(0,1)#to insert the elsement at the index like 0th index per 1 add kar diya 
print(list)

value=list.pop(6)#it removes the element from the particular index
print(value)
print(list)

list.remove(9)#it removes dirt value from the list 
print(list)

print("----------------------------tuple--------------------------------------")

#tuples are immutable like string tuples can be create using '( )'this tuples can not be changed 
a=(1,2,False,"bmw","audi")
print(type(a))

b=(1)#it ouput will class<int> because pyhton undersatnd you put a elment in tuple  but if want to create empty tuple you can use ',' after the element 
print(type(b))

c=(1,)
print(type(c))#booooom its type tuple 

#methods on tuple

mytuple=(1,2,35,5456,False,"bmw","audi",1)
print(mytuple.index(False))#it can be return the index value of the particular element 

print(mytuple.count(1))#it returns item no of times in a tuple 

print(len(mytuple))#prints the length of the tuple 

tup=(1,5,6,9,4,3)
print(max(tup))#it can only apply on integer value like (1,2,3,-1,-6....etc)

tup=(1,5,6,9,4,3)
print(min(tup))

print("bmw" in mytuple)#by using this we can check is it element can be exist in the tuple or not it gives the output in true or false 
