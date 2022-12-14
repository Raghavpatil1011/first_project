#simple calculator
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def sq_root(b):
    return b ** 0.5
while True:


# print
#Select operation
#1.Add
#2.Subtract
#3.Multiply
#4.Divide
#5.Exit
#6.square root

   ''' choice = int(input('Enter the operation choice you  '))
    if choice == (1,2,3,4,5):
        a = int(input('Enter the num1\n'))
        b = int(input('Enter the num2\n'))
        if choice == 1:
            print(add(a,b))
        elif choice == 2:
            print(subtract(a,b))
        elif choice ==3:
            print(multiply(a,b))
        elif choice ==4:
            e = divide(a,b)
            print(e)
            f = int(input('if you want answer in int enter 1 or to continue enter 0 '))
            if f == 1:
                print(f"{e:.2f}")
            else:
                break

        elif choice ==5:
            break'''




b = int(input('Enter the number'))
print(sq_root(b))