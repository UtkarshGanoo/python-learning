# exception and errror two differnt things hoti h agr error aata h toh jis line mai error hai uske niche ka code bilkul nahi chalega or 
# exection ko try and execpt ki help se handle kar sakte h try mai code likhte hai ager code chal gayatoh koi baat nahi ager wrong input h toh usee
# except ki help se invalid input show karke  baki code ko terminate hone se bacha skate h isse koi eroor genrate nahi hoti hai kisi particular error 
# ke liye bhi show kara skte h jaise type error value error and zerodivisionerror apn error ki raise bhi kara skate hai jisse devloper ko pata chale 
# ki usne kya mistake kiya h try&else jab try success hoga tabhi else chalega warna nahi chalega 




"""iise code mai ager integer input nahi kiya uske jagh string ya koi other input diya toh ye iss trah ki error shoe karega jissa yah 
devloper ki mistake mani jayegi 

a =int(input("enter a no: "))
print(a)"""

"""iss code mai try wale block jab execute hoga jab code mai input shai hoga toh except wala block ko ignor kar dega  or uske niche ka code execute 
karne chala jayega code emai integer input manga hai agar integer ki jagh string ya other diya hai toh execpt wala block chalega or invalud input show 
karega  

try:
    a =int(input("enter a no: "))
    print(a)
    print("congrtulation you are signed in ")
except Exception as e:
    print("invalid input ") """

#different type error handling 
"""here we handle two type eror first zerodivision error and secound value error 
try:
    num=int(input("enter a number: "))
    result=10/0
    print(result)
except ZeroDivisionError as z:
    print("you can not divide by zero")
except ValueError as v:
    print("please enter valid value ")"""

# raise error
"""
a =int(input("enter a num: "))
b =int(input("enter a second num: "))
if (b==0):
    raise ZeroDivisionError("you cant divide by zero ")
else:
    print(f"the divide of a and b is {a/b}")"""

# try and else 
"""isme ager try wala succesful execute hoga tabhi else wala per jayega nahi toh nahi jayega 
try:
    a= int(input("enter a no: "))
    print(a)
except Exception as e:
    print(e)
else :
    print("i am only work with try block")"""

# finally 
"""finally ka mainy use fution mai hota h ager finallly nahi likha hai or function ke methods ko return kar diya toh uske niche ka matlab metods ke 
bahar ka code nahi chalega ager methods ke bahar finaly ke inside code likha hai toh woh jarur chalega hi 
def main():
    try:
        a= int(input("enter a no: "))
        print(a)
        return #ager finally nahi likha or direct retunr kar diya toh input lrtr print karke bahara ho jayega
    except Exception as e:
        print(e)
        return 
    finally:
        print("only when you give me respect when i am running ")
main()"""