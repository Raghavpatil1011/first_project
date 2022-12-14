

#lambda function: is a small  anonymous fn: why anonymous cuz their is no name given  for function.
'''a lamda fn can take n numbers of arguments but can only one expession
syntax
lambda arguments:expression'''
#eg1.
x=lambda a:a+10
print(x(5))

#eg.2
#can give as many arguments but one expression
x=lambda a,b,c,d:a+10+b+c+d    #a,b,c,d= agruments and a+10+b+c+d = expression
print(x(5,10,20,30))

#eg.3
#lambda fn can also use for string
x=lambda a:a.upper()
print(x("balck"))

#eg.4
#can use for list also
l1=[1,5,4,6,8,10,9]
new_l=list(filter(lambda x:(x%2==0),l1)) #x will be take each from l1
print(new_l)
new_l2=list(filter(lambda x:(x>4),l1))
print(new_l2)
#print prime numbers by lambda fn.
for i in range(2,10):
   new_l3=list(filter(lambda x:x == i or x % i,l1))
print(new_l3)

#MAP
#mapping an operation to older lists
#eg.1
l1=[1,2,3,5,78]
new_l1=list(map(lambda x:x*2,l1))
print(new_l1)

#eg.2
subject_marks=[("english",90),("math",45),("science",90)]
subject_marks.sort(key=lambda x:x[0])
print(subject_marks)

#1. wpp to create a lambda fn that adds 15 to agiven number passed as an arguement?
#2. wpp to filter a list of integers from given list.
#3. wpp to square and cube every number in a list of integers using lambda
#4. wpp to check whether a given string is number or no.
#5. wpp to count even odd numbers  in a given array of integers
#6. wpp to find lowest grade of any student from given names using list and lambda



#lambda function
str=input("enter the string")
x = lambda a:a.upper()[::-1]
print(x(str))

#1.
inp = int(input("enter the value"))

x = lambda a:a*15
print(x(inp))

y=float(input("enter the value"))
x=int(input("enter the value"))
a = lambda num:"its integer" if isinstance(num,int) else "float"
#isinstance will check num or int
print(a(y))
print(a(x))
print(a(2))
print(a(9.7))


a= int(input('enter the value'))
b = int(input('enter the value'))
x= lambda num,num1:"bigger" if num>num1 else "smaller"

is_even=[lambda a=i:a*10 for i in range(1,10)]
for x in is_even:
    print(x())

is_even=[lambda a=i:a  for i in range(1,10)]
for x in is_even:
    print(x())

# wpp with arguments and expression using lamda fn
# give 2 example of lambda fn using if
# give 2 example of lambda fn using for