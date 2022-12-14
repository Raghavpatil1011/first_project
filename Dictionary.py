
#dictionary- key,value pair
#represented by {}
#ordered, from 3.6 version it is ordered ..... earlier it wasn't
#it can hold different datatypes
#dictionary cannot have duplicate keys
#mutable:changable
#have a list inside dictionary
#1 key can hold multiple value
a= {"name":"nikil","age":28}
print(a)
print(len(a)) #each key value will count as one data
print(type(a))
#two ways to withdraw data
print(a["age"]) #print(a("age")) will give error
print(a.get("age"))

print(a.keys())
print(a.values())
print(a.items()) #withdraw both keys and values
#adding new value
a["color"]="black"
print(a)
#update  the value
a["age"]=60
print(a)
a.update({"name":"niya"})
print(a)
#delete the value
a.pop("color")
print(a)
a.popitem() #remove the last item of dictionary
print(a)
b={"a":1,"b":2,"c":3,"d":4}
print(b)

del b["a"]
print(b)

'''del b
print(b)''' #give an error cuz "del" deleted "b"
#difference btw del and clear is
#del: will delete whole dictonary
#clear: will delete only items brackets will still gonna be present
a.clear()
print(a) #will print {}

a={"names":{"python":["a","b","c"],"java":["d","e","f"]},"class":"online"}
print(a["names"]["python"][0]) #to print "a"

#question to practice
#1.is it possible to convert 2 list to dictionary if yes - how?
#2.merge 2 dictionary to one
#3.print the value of key "history" from below dict
# q: change the value of physics exist in dictionary
d1={
    "class":{"student":
                 {
                     "name": "mike",
                      "marks":{
                          "physics": 70,
                          "history":80

                      }
                 }   }
}
'''print(d1["class"]["history"][0])'''
#4.write a python program to create a new dictionary by extracting the mentioned keys from below dictionary
d1={
     "name":"hari",
      "age":20,
"salary":10000,
"city":"delhi",
}
#5.keys=["name","salary"]
#delete a list of keys frm above dictionary
#6.keys =["name","salary"]
#check if a value exist in dictionary
#rename name key with names

'''#2 by me
def merge(dict_1,dict_2):
dict_1={"a":10,"b":20}
dict_2={"c":30,"d":40}
print(merge(dict_1,dict_2))'''

