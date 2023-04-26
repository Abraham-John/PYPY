def add(A,B):
    return(A+B)
def subtract(A,B):
    return(A-B)
def multiply(A,B):
    return(A*B)
def divide(A,B):
    return(A/B)

print("Please select the operatation")
print("a. Add")
print("b. subtract")
print("c. multiply")
print("d. divide")

p = input("Please enter choice (a/b/c/d):   ")

x = float(input("Enter first number.\n"))
y = float(input("Enter second number.\n"))

if p == 'a':
    print(add(x,y))
elif p == 'b':
    print(subtract(x,y))
elif p == 'c':
    print(multiply(x,y))
elif p == 'd':
    print(divide(x,y))
else:
    print("Invalid input")