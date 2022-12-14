x = 1
y = 0
z = 0
if y or x and z:
    print("yes")
else:
    print("no")


for i in range(2):
    print(i,end=" ")
for i in range(4,6):
    print(i, end=" ")


true = False
while True:
    print(True)
    break
#input from user
a = int(input("enter your num"))
print(a)
print(a+100)


name=input("enter name")
print("the name is"+name)

#collect user details name,age,phno.,add,marke1,mark2,mark3
#the name is _
#the age is _\
#the phnum is_
#the total marks is _


name = input("Enter your name: ")
age = input("Enter you age: ")
phnum = input("Enter you phone no: ")
address = input("Enter your address: ")
mark_1 = input("Enter mark 1: ")
mark_2 = input("Enter mark 2: ")
mark_3 = input("Enter mark 3: ")



tot_mrks = int(mark_1) + int(mark_2) + int(mark_3)



print("The name is:", name)
print("The age is:", age)
print("The phone no is:", phnum)
print("The total marks is:", tot_mrks)




#question2
#create a simple billing
#define price of each vegetables inside variables
#collect input from user which vegetable they want
#collect input from user how many kg they want
#then display the total price of that product
#after taking all vegetables calculate total bill also

#a=20#rate of 1kg of beans
#beans=int(input("enter the weight of beans;"))
#b=30#rate of 1kg of onion
#onion=int(input("ehter the weight of onion "))
#c=10#rate of 1kg of potato
#potato=int(input("enter the weight of potato;"))
#price1=a*beans
#price2=b*onion
#price3=c*potato
#total_bill=price1+price2+price3
#print("the total bill amount is",total_bill)
#question3

#give balance = 50000
#think you are inside atm
#print -welcome to atm
#take input from user how many amount they want to withdraw
#change balance with substracting amount withdraw
#then print the final balance
#try to deposit amount
 #   add amount with balance
  #  again print balance
#in last print thankyou visit again
#balance=50000
#print("welcome to ATM")
#a=int(input("the amount to withdraw",amount))
#ew_balance=balance-a
#print("the new balance is",new_balance)
#deposit=20000
#c= new_balance+deposit
#print("final balance",c)
#print("thankyou visit again")

balance = 50000
print("Welcome to ATM")
atm = int(input("how much amount you want to withdrawl"))
print("please collect your case")
update1 = balance-atm
print("your remaining balance is ",update1)
deposit = int(input("how  uch of amount you want to deposit"))
print("your cash is succesfully deposited")
update2 = update1+deposit
print("your balance is updated to ",update2)
