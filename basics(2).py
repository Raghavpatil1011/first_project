#the print is used to output variables.
x= "hello"
z="take"
y= "bye"
print(x,y,z)
print(x+y+z)
print(x+" "+y+" "+z)
a="10"
b="20"
print(a+b)
x=10
y="1"
print(x+y)
#find the sum of two numbers and print the result stored in another variable
#find average of two numbers
#save subjects marks in different variable then find the total mark, percentage scored
a=29
b=56
c=a+b
print(c)


def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))
print(absolute_value(-4))

m=2
total=0
while(m<6):
    total=total+m
    m=m+1
print(total)

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)


while True:
    print(True)
    break

if (10 < 0) and (0 < -10):
    print("A")
elif (10 > 0) or False:
    print("B")
else:
    print("C")

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)
