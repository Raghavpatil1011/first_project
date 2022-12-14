# i
#ITERATORS AND GENRATORS
'''for iterating we have for loop and while loop
another object is iterator for iterating
lazy way for iterating'''

#eg.1 with lists
x = [25,78,'coding','is','<3']
a = iter(x)
print(next(a)) #you have to print again n again to iterate
print(next(a))

#eg.2 with strings
x = "i am from class"
a = iter(x)
print(next(a))
print(next(a))
print(next(a))

#lets create cutomize iterator

#to give number by exponents
class A:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=2 ** self.a
        self.a+=1
        return x
abc=A()
y=iter(abc)
print(next(y))
print(next(y))
print(next(y))

#to give number by adding 1 to it
class A:
    def __iter__(self):
        self.a+=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
abc=A()
y=iter(abc)
print(next(y))
print(next(y))
print(next(y))



class A:
    def __iter__(self):
        self.a=0
        return self
    def __next__(self):
        if self.a % 2 == 0:
            x=self.a
            self.a+=1
            return x
        else:
            return "odd"

abc=A()
y=iter(abc)
print(next(y))
print(next(y))
print(next(y))
