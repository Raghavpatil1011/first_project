#iteration on dictionary

#eg.1
details={"user1":"lion","user2":"cat","user3":"monkey"}
for i in details:
#below both print comand will give both keys and values
    print(i) #will print keys
    print(details[i]) #will give value in dictionary
#another way of getting values in dictionary
for i in details.values():
    print(i)
#print both keys and values
for i,j in details.items():
    print(i,details[i])
    print(i)
    print(j)

'''user registration format a login page
whenever a user is registering with username and password it should  get saved inside a dictionary
in case of login the page as to check whether user and password is available in dictionary'''
#dict1={"user1":1234,"user":4567}

dict_1={"Monica":{"NAME":"Monica","AGE":22,"PHONE NO.":7234},
        "Rachel":{"NAME": "Rachel","AGE":23,"PHONE NO.":9876},
        "Chandler":{"NAME":"Chandler","AGE":22,"PHONE NO.":3456},
        "Ross":{"NAME":"Ross","AGE":25,"PHONE NO.":7654},
        "Joey":{"NAME":"Joey","AGE":24,"PHONE NO.":3487}
        }

print('''                            
                                     ----------------------------------------
                                     ----------------------------------------
                                                 !!!!WELCOME!!!!
                                                ENTER 1 FOR LOG_IN
                                               ENTER 2 FOR REGISTRATION
                                     ----------------------------------------
                                     ----------------------------------------''')
inp1=int(input("Enter the input:"))

if inp1==2:
    print('''                          
                                     ----------------------------------------
                                     ----------------------------------------
                                               !!NEW REGISTRATION!!
                                     -----------------------------------------
                                     -----------------------------------------''')
'''name=input("Enter your Name:  ")
age=int(input("Enter your Age: "))
phone_no.=int(input("Enter your Phone No.: "))
dict_1.update({"NAME":{"fname"}={"name"},}})
print("your password is 1234")'''
print('''                            
                                     ------------------------------------------
                                     ------------------------------------------
                                          !!! REGISTRATION COMPLETED!!! 
                                     ------------------------------------------
                                     ------------------------------------------''')