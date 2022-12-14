'''a = int(input("Enter the number of elements\n"))
print("Enter the elements")
b = []
for i in range(0, a):
    b.append(input())
while True:

    print("Menu")
    print("1.Display the elements")
    print("2.Next element")
    print("3.Previous element")
    print("4.Exit")
    c = int(input("Enter your choice"))
    if c == 1:
        print("The elements are :")
        for i in b:
            print(i)
    elif c == 2:
        x = iter(b)
        try:
            d = int(input("Enter the position of the element to find the next value:\n"))
            q = b[d + 1]
            print("The position of new iterator using next() is :", q)
        except Exception:
            pass

    elif c == 3:
        try:

            e = int(input("Enter the position of the element to find the prev value:\n"))
            w = b[e - 1]
            if w == b[0]:
                pass
            else:
                print("The position of new iterator using prev() is :", w)
        except Exception:
            pass'''


'''city = int(input('enter num1')); country =int(input('enter num2'))
print(city,country)'''

#print( "{0} is {1} years old".format(name,age))

'''z='s'
x= ('enter your name'+z)
y = ('enter your age'+z)
print(x)
print(y)
print('{name} is {age} years old'.format(name=x,age=y))'''
#import keyword
#print(keyword.kwlist)
#1
'''pi = 3.14
r = int(input('enter the radius of sphere'))
volume = pi*(r**3)
v=('the vloume of sphere is ',volume)
print(v)'''
#4
'''f= int(input('enter the fahrenheeit'))
c=(f-32)*5/9
print(c)'''
a = 2**2**2**2
print(a)