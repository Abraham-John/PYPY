
from sys import float_repr_style


a = float(input("Enter first Number.\n"))
b = float(input("Enter second Number.\n"))
c = float(input("Enter third Number.\n"))

if  (a>b) and (a>c): 
    largest = a
elif (b>a) and (b>c):
    largest = b
else:
    largest = c

print("The largest number is",largest)
