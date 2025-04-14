# it is immutable if we can using functions in string and changing it but then we print original string it give that what we intialize first
# a string can be craete using like '("")' this and '(' ')'this and by default all values first cna automatically a string 
name="utkarsh"
name1="UTKARSH is an enthrpuner"
age=28
name[0:7]#same like array first index include '0' but last index last charecter +1 type karte hai or woh ek less chalta h like 6'' tak
print(name)

print(name[-6:-1])#convert it into +ve first 
print(name[1:7])
print(name[:7])# it means 0 to last but -1 like 6  but this and line no 8 output will diffrent because line no 8 has define starting charecter of string
print(name[1:])# it means 1 to last but -1 like 6 
print(name[0:7:4])# it will skips the value
#this are the output
'''utkarsh
tkars
tkarsh
utkarsh
tkarsh
ur'''

# function of string
print(len(name))#it give the length of string(no. of character)
print(name.endswith("ars"))#it gives the output in true or false if the string can ends with that we give in bracket it give true otherwise false
print(name.startswith("utk"))#it gives the output in true or false if the string can starts with that we give in bracket it give true otherwise false
print(name.capitalize())#it can capatilize only strating character 
print(name.upper())
print(name.lower())
print(name1.replace("enthrpuner","succsseful businessman"))
print(name1.find("an"))
print(name1.split())
print("ganoo".join(["utkarsh ","enthrpuner"]))
print("utkarsh ganoo",format(age))
