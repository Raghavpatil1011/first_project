
# function: block of code, it runs only if it is called
#eg.1
def withdraw(): #def is used to define a function.
    balance=50000
    withdraw= int(input("enter teh amount u want to withdraw"))
    balance -= withdraw
    print("the new balance is", balance)
withdraw() #to get output we have call function
print("thankyou visit again")
withdraw() #we dont have to write a whole code again we can juss call the function.

#eg.2
def withdraw(): #def is used to define a function.
    balance=50000
    withdraw= int(input("enter teh amount u want to withdraw"))
    balance -= withdraw
    name = "nithya"
    # .format : replace the curly braces with the variables.
    #if we give number in braces then it will work acc. to indexing.
    print("the amount withdrawed is{1} and the balance is {2}.my name is {1}".format(withdraw, balance,name))
withdraw() #to get output we have call function
print("thankyou visit again")
withdraw() #we dont have to write a whole code again we can juss call the function.


#parameter passing.

#eg.1
def sum(a,b):
    add=a+b
    print("the values {}{} sum is {}".format(a,b,add))
sum(10,9)
print("its done")
sum(8,10)

#eg2.
def sum(a,b=10): #its default value.
    add=a+b
    print("the values {}{} sum is {}".format(a,b,add))
sum(10)
print("its done")
sum(8)