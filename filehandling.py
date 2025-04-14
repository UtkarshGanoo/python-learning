
"""file_nameopen() is to use open the file 
file_name.read()is use to reaad the data of the file
.close() is to use close the file because its medtory to close the file 
int this there are many type of function like readlines()it can read all line and it can give in the list form
readline()it can give the one line at a time how much time will you use this method it can read line that much time
there are many type of modes in file handling ( 'r' for read , 'w' for write , 'a' for open fro appending"last mai add karti jayegi " ,  '+-'open for updating , 'rb' for read in binary mode, 'rt' read in text mode )
# with ke use se multiple files ko bhi open kar sakte h 
"""


""" 
#this is use to read the file open function can get 2 parameter 1st get the file name and 2nd get the  mode of the 
# file mode means read("r") or write ("w") by default the file mode is read 
f=open("first.py")
# f=open("first.py","r") like that open function can get 2 parameter
data=f.read()
print(data)
f.close()"""

"""
# now here we can write in a file here we use
content="hi utkarsh you are practicing to file input and output and here you are write in a file with using python concept" 
f=open("myfile.txt","w")
f.write(content)
f.close()
#and read the myfile.text
u=open("myfile.txt")
print(u.read())
u.close()"""


"""a=open("myfile.txt")
print(a.readlines())
print(type(a.readlines()))
print(type(a.readlines()))"""

"""a=open("myfile.txt")
print(a.readline())
print(type(a.readline()))
a1=a.readline()
print(a1,type(a1))
a2=a.readline()
print(a2,type(a2))
a3=a.readline()
print(a3,type(a3))"""

"""line=open("myfile.txt")
f=line.readline()
while(f!=""):
    print(f)
    f=line.readline()
line.close()"""

#iske use se file close karne ki jarurat nahi hoti h file automatically read write hoke close ho jayegi
"""with open("myfile.txt") as f:
    print(f.read())"""


with (
    open("myfile.txt") as f1,
    open("myfile.txt") as f2
):
     content1 = f1.readline()
     content2 = f2.read()
     print("First Line:", content1)
     print("Full Content:", content2)