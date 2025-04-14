# kisi existing list ki help se new list create karne ka elegent way hota h ager without list comprihansion ka use karte hai toh kisi new list ko crete karne ke liye 
# loops ki help se bahut bada code ho jata hi isko reduce karene ke liye list comprihansiton aaya iaka syntax ye hota hai ("new_list = [expression for item in iterable if condition]")
# expression → The operation to perform on each item iterable → The collection (like a list, range, or string) 
# condition (optional) → Filters elements based on a condition.

# without list comnprihansion 
"""mylist = [1,3,5,6,3,4]
sqr_list=[]
for item in mylist:
    sqr_list.append(item*item)
print(sqr_list)"""
    
# with list comprihansion
"""lsit =[1,2,3,4,5]
new_lsit=[i*i for i in lsit]
print(new_lsit)"""