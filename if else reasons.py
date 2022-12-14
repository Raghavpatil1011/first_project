#why to use if-elif ,why not if-if

#FOR: used for looping,iterating

#eg.1
a=["apple","orange","kiwi"]
for i in a:
    print("the fruits are",i) #will give each value from list, dictionary, set
    s=i+"good fruit"
    print(s) #can make changes

#eg.2
for i in "apple": #will take each character of string i.e., iterate each character
    print(i)

#eg.3
f=["red",'orange',"yellow","bule"]
for i in f:
    if i=="orange":
        print("i love this color",i)
        break
print("i found my color")

#eg.4
for i in f:
    #print(i) #will print red only due to break
    if i=="orange":

        break
    print(i) #will print red, orange

#eg.5
for i in f:
   # print(i)
    if i=="orange":

        continue #will skip current condition and go with further
    print(i)
