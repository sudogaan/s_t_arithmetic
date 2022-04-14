# Numbers: int, float, complex
# Operations: + _ * /
x = 28 #int
y = 28.0 #float 

#ints are narrower than floats

x = 1.732 #float
print(x + 0j)
complex(1.732) #converting a float into a complex number)

#Arithmetic Operations

a = 2 #int
b = 6.0 #float
c = 12 + 0j #complex number

#Rule: Widen numbers so they're the same type 

#Addition
print(a+b) #floats are wider than ints so the result is 8 as a float not 8 as an int

#Subtraction
print(b-a) #ints are narrower than float so python widens 8 to a float than subtracts and the result is float

#Multiplication
print(a*7) # int * int

#Division
print(c/b) #floats are narrower than complex numbers so b is widened to a complex number before the division and the result is a complex number
#16/5 gives float even both of them are ints
# % gives the remainder
