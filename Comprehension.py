#LIST COMPREHENSION: different ways to create a list
#is a shorter syntax to create a list
l1 = ['80','90','60','a','b','c','d']
nwlist=[]
for i in l1:
    if '90' in i: #will append this a in nwlist
        nwlist.append(i)
print(nwlist)

#syntax for one line code
#[expression for item in iterable if condition ==  True]
nwlist= [i for i in l1 if i == '90']
print(nwlist)

nwl2 =[x for x in range(10) if x>5]
print(nwl2)
a = ['anu','manu','jeo']
nwl3=[x.upper() for x in a if 'a' in x]
print(nwl3)

fruits = ['apple','banana','grapes','orange']
nwlst=[x if x!= 'banana' else 'i dont like banana'for x in fruits ]
print(nwlst)
#returns item if its banana or it will return i dont like banana

l1=[1,2,3,4,5]
l2=[5,6,2,3,4]
result=[(a,b) for a in l1  for b in l2 if a==b]
print(result)

#questions
#1. find all numbers 1-100 divisible by 7
#2. count n: of space in a string
#3. get numbers from sentence
#4. find all words in alist that are less than 4

#1.
div7 = [x for x in range(1,100) if x % 7==0]
print(div7)

#2.
strng = "hello annu and bye annu"
space = [x for x in strng if x==' ']
print(len(space))

#4.
lst = ['rachel','ross','joey','phoebe','cahndler','eve','emma']
result = [word for word in lst if len(word)<4]
print(result)
