#arthemetic operator
x=4
y=3
z=2
a=x-y%z
print(z)

p=2
q=6
r=3
s=r*q**p
print(s)

x=25
y=2
z=3
k=x**y%z
print(k)

#assignment operator
b=7
b*=4
c=2
c**=3
print(b,c)

e=6
e/=2
f=24
f//=5
print(e,f)

e=45
e/=2
f=37
f//=6
print(e,f)


#comparison operator
a=6
b=8
print(a>=b)

x=4
y=6
print(x==y)
print(x<y)

a=2
b=4
print(a!=b)


#logical operator
z=0
q=4
print(z<b and q>z)

a = 10
b = -10
c = 0
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")


#indentity operator
a = 20
b = 20

if ( a is b ):
   print ("Line 1 - a and b have same identity")
else:
   print ("Line 1 - a and b do not have same identity")

x=6
y=65
z=x
print(id(x))
print(id(y))
print(x is y)
print(z is y)


x = '101'
y = '101'
if x is y:
  print ('x is y')
else:
  print ('x is not y')

#membership operator
a='hello world'
print('world' in a)

x=24
list=[10,20,30,40]
if x in list:
    print("x is present in given list")
else:
    print("x is not present in given list")