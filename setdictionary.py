#dictionary is aslo store the  data like string list tuple but its difrent it can store the key vlaue pair in it .it is a mutable it can not contain duplicate
#value key ke corresponding value ko direct show karne ke liye dictionary ka concept aaya jisse keval key ka naam deke usse related vlaues ko dekh sakte h

dic={
    "utkarsh":{
        "mobileno":9575335089 , "gender":"men" , "occupation":"student" 
    },

    "poorva":{
        "mobileno":9893201836 , "gender":"women", "occupation":"supervisor"
     },

    "meena":{
        "mobileno":7470692841 , "gender":"female","occupation":"supervisor"
        },

    "uday":{
        "mobileno":8982746916 , "gender":"male", "occupation":"supervisor"
        }
}
print(dic["utkarsh"])
print(dic["uday"])

print(len(dic))
print("-------------------------------------------------------------------------------------")

#methods of dictionary

dic1={
    "cow":124421,
    "dog":754854,
    "cat":89827
}

print(dic1.items())#return the list values
print(dic1.keys())#return the keys 
dic1.update({"cat":888888,"poorva":121212})#by using this we can change or add key value 
print(dic1)
print(dic1.get("cow"))#if the key will exist in dictionary it return the value of the key if not exist it returns none 
print(dic1["dog"])#if the key will exist in dictionary it return the value of the key if not exist it returns error msg 
print(dic1.popitem())# it give last inserted keyvalue pair

print("--------------------------------sets------------------------------------------------")

#in the set can not contain repetative element  we can create empty set using 'set( )'this set and dictionary mai elemnet '{ }' iske inside hi dalte h 
# set or dictoinary same type se banaye jate h but ager sidhe {}laga ke element dal do to woh set honge or {"key":vlaue } to ye dictionary hoga 
# set mai list nahi dalna chahiye because set mai index namm ka concept nahi hota jissa update nahi kar sakte 
dic2={1,2,3,4}
print(type(dic2))

myset=set()
print(type(myset))

setts={1,2,5,8,5,6,2}
print(setts)

#methods of set 
ses={1,2,5,8,5,"bmw"}
ses.add("audi")#add the elelment in set
print(ses)
print(len(ses))
ses.remove(5)#it remove the element 
print(ses)


uni={1,2,5,4,8,6,5,4,6}
inter={1,6,9,8,7}
print(uni.union(inter))
print(inter.intersection(inter))
