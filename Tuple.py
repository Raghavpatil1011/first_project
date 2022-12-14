
'''TUPLE-represented by()
multiline items can be stored
ordered index no:
it also support different datatype
tuple is immutable
tuple is faster
unpacking: extracting the values back in to variables'''

a=(1,"abcd",2,4)
print(type(a))
print(a[2]) #to retrieve a item
#a[2]="red"
print(a) #replacement is impossible
#for add item in tuple convert it into list or add two tuple

b=list(a)
print(b)
print(tuple(b))
a=(1,"abcde",3,4)
b=("ball",)
a+=b
print(a)

#how to remove an item
a=("a","bd",2,6,7)
c=list(a)
c.remove("a")
b=tuple(c)
print(b)
#del deleting entire tuple
#del a
#print(a)

#example of unpacking
tuple1=(1,"abcd",2,4)
(x,y,z,o)=tuple1
print(x)
print(y)
(x,*y)=tuple1 # * will hold mutiple value
print(x)
print(y)

t1=(1,2,3)
t2=(3,4,5)
t3=t1+t2
print(t3)
t3=t1*3
print(t3)
#t3=t1**2