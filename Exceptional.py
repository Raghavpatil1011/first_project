
#EXCEPTION HANDLING :
#3 Types
#1. compile time error/syntax error  for e.g. you have given print only withot brackets so it will through an error
#print(
#2. logical error #we find this error in testing of software development
#addition of 2 numbers
#a = '10'
#b = '20'
#sum = a+b
#3. run time error : #occurs by the user not developver, exception handling deal with run time error

#divide your entire program into 2 parts
#1.complex : is a where user can make error
#b = int(input('enter num'))
#2.normal statement : is a where an external user can't make an error
#a = 20 # only  developver can make changes and error in this but not user

'''a = 10 #normal statement
b = int(input('enter num')) #complex statement
res = a/b #it is getting stopped here if we input 0
print('bye')'''

#HOW TO HANDLE THIS TYPE OF EXCEPTION
#put user input under try:

'''a = 10
try:
    a = int(input('enter your num')) #error
    b = int(input('enter num')) # error
    if a>5:
       res = a/b
    print(res)  #throw error if res is not computed
#in thi case it will not going to stop here

except ZeroDivisionError as b:
    print('please be careful dont give 0')
except ValueError as c:
    print('plz enter integer num',c)
except Exception as e:
    print('error not defined')

print('bye')'''

#raising an exception of our own
try:
    x = int(input('enter the amount to withdraw'))

    if x < 500:
        raise Exception('plz enter amount abov 500')

except Exception as e:
    print(e)

else:

    print('thank you visit again')


