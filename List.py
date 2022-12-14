name= "hello! my name is karen"
print("in" in name)
#list- represented by [1,2,3]
a=[1,2,3]
b=["a",12,13,"b"]#items of different datatype
c=["apple", "orange","grape","apple"] #list allow duplicates
print(c[2])#the list is ordered with index no; index number starts with 0
print(len(c))#it counts the number of items inside the list
print(c[2:4])
print(c[1:])#orange,grape,apple
print(c[-3:-1])#grape,apple
#create a list of colours, retrieve black and orange colour from it , retrieve colours in the range 2 to 5, retrieve last
#3 items using negative indexing
a=["black","purple","orange","pink","red","blue"]
print(a[0])
print(a[2])
print(a[2:5])
print(a[-1:])
c[2]="pineapple"
print(c)#list is mutable
c[2:4]=[1,2]
print(c)
c.insert(2,"juice") #will insert a value at index 2 and rest will shift to right
print(c)
c.append("veg") #will add in last
print(c)
b.extend(c) #will add two lists
print(b)
#4 ways in which we can insert a value insert,append,extend, updating with other value
#example1
a=["pens","cars","books","pencils"]
a[3]="sketchpens"
print(a)
a.insert(3,"chips")
print(a)
a.append("1")#take only one arguement
print(a)
b=[12,13,34]
b.extend(a)
print(b)

#example2
prime_numbers=[2,3,5,7]
prime_numbers.insert(4,11)
print('list:',prime_numbers)
#4 ways to remove something from lists: pop,remove,del,clear
x=[1,2,3]
y=[4,5]
x.extend(y)
print(x)
x.remove(2)#will take item name
print(x)
x.pop(1)#index no:1
print(x)
x.pop()#if index number is not provided it will remove last item
print(x)
del x[0]
print(x)
'''del x[3] #index error will give
print(x)
k=[12,13,14,15,16]
del k #if index not provide it will delet entire list
print(k)'''
l=[40,50,80]
l.clear()#remove only the items from list and it will contain empty list
print(l)

#questions for practice
#1. check whether a item exist in a list
#2. write a program to sum all items in a list
#3. wpp to find the largest
#4. wpp to print a list after removing oth, 4th and 5th elements
#5. reverse a list in python
#6. add anew item to list after a specified item
#7. replace a list value with new value
#8. split a list in half and store elements in 2 different list


a=[1,2,"apple","grapes"]
print("kiwi" in a)

list1=[1,4,8,9,3]
print(sum(list1))

list2=[134,678,904,234,456,98]
print(max(list2))

list3=[8,4,"black","pink","red",34]
list3.remove(8)
list3.remove("red")
list3.remove(34)
print(list3)

lt_4=[123,'a',67,'b']
lt_4.reverse()
print(lt_4)

list3.insert(2,38)
print(list3)

list3[3]="green"
print(list3)

list6=[1,2,3,4,5,6,7,8,9]
length=len(list6)
mid_half=length//2
first_half=list1[:mid_half]
sec_half=list1[mid_half:]
print(first_half)
print(sec_half)


#list5=["a","b","c","d","e"]
#print(sum(list5)) #will give error
