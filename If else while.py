x = True
y = False
z = False
if x or y and z:
    print("Hello")
else:
    print("World")

for i in range(10):
    if i == 5:
       break
    else:
        print(i, end=" ")
else:
    print("Here")


i = 1
while True:
    if i%3 == 0:
        break
    print(i,end=" ")
    i+=1

x = True
y = False
z = False
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)

if True or True:
    if False and True or False:
        print('A')
    elif False and False or True and True:
        print('B')
    else:
        print('C')
else:
    print('D')

i = 1
while i<12:
    if i%2 == 0:
        break
    print(i, end=" ")
    i += 2

i = 5
while True:
    if i%0o11 == 0:
        break
    print(i, end=" ")
    i += 1
