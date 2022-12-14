
#SET= represent by {}
#unordered
#unchangeable
#any datatype
#do not allow duplicates
myset={"apple","banana","orange","kiwi"}
print(myset)
print(len(myset))
print(type(myset)) #any datatype
x=("apple","k","l")
y=(set(x))
print(y)
#once aset is created you cannot change data inside it but uh can add new data
y.add("orange")
print(y)
#update function helps to add two sets
y.update(myset)
print(y)
#delete items
y.remove("apple")
print(y)
y.discard("k")
print(y)
#difference btw "remove" and "discard"
#if the item is remove is not present it  will give an error
'''y.clear()
del y
print(y)'''
y.pop()
print(y)# it will remove any random element
#intersection: take common value
#union: take all value from both set

set1={1,2,3}
set2={3,4,5,6}
set3=set1.union(set2)
print(set3)
set4=set1.intersection(set2)
print(set4)
#returns a set that contains the items from set 1 but will not give value of set2
set5=set1.difference(set2)
print(set5)
#SUBSET
a={1,2,3,4,5} #superset
b={4,5} #subset
c={9.4,5}
print(b.issubset(a))
print(c.issubset(a))
print(a.issuperset(b))
print(a.issuperset(c))
#1. check whether a item is present in set
#2. wpp to create a set
#3. wpp to remove item from set
#4. wpp to remove item from set if its present in set
#5. wpp to do union of sets
#6. take two input from user and check whether its a subset of other
#7. remove all elements from set
#8. find the length of a set
#9. wpp to check two sets don't have common item
#if,elif and else
a=10
if a>=10:
    print("good")
elif a<10:
    print("bad")
else:
    print("no chance")

'''1. collect student mark and print distiction if mark btw 89-100
print firstclass if mark  btw 60-80
print secondclass if btw 45-60
or print failed'''
#2. give num odd or even
#3. give num +ve ,-ve or 0
#4. give num is one digit ,two digit or 3 digit
#5. print whether num is smallest 4 digit number
#6. given num is divisible by 5
#7. find max but out of 3 numbers

#1
mark1=int(input("enter marks of subject"))

if mark1>=80 and mark1<=100:
    print("distiction")
elif mark1>=60 and mark1<=80:
    print("firstclass")
elif mark1>=45 and mark1<=60:
    print("secondclass")
else:
    print("failed")

#2.
num= int(input("enter 1st number"))

if num%2==0:
    print("it is EVEN number")
else:
    print("it is ODD number")

#3.
num1=float(input("enter a number"))
if num1>0:
    print("it is positive number")
elif num1==0:
    print("it is zero!")
else:
    print("it is negative")

#4.
num2=(input("enter a number"))
length=len(num2)
if length==1:
    print("one digit number")
elif length==2:
    print("two digit number")
elif length==3:
    print("three digit number")
