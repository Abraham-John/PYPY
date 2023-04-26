'''#1

print("Hello World")

#2

age = 69
price = 19.50   
first_name = "John"
print(age,price,first_name)
print(age + price)
print(age) 

name = "Abraham John"
age = 15 
status = "New employee"
print(name)
print(age)
print(status)
print(name,age,status)

#3

name = input("What Is Your Name ?\n")
print("Hello " + name)

#4

birth_year = input("Enter Birth Year: \n")
age = 2022 - int(birth_year)
print(age)

#5

a = int(input("Enter first number.\n"))
b = float(input("Enter second number.\n"))
print("sum : " , a+b)
print("difference : " , a-b)

#6

first = input("first :")
second = input("second :")
sum = float(first) + float(second)     
print("sum : " + str(sum))

#or

first = float(input("first :"))
second = float(input("second :"))
sum = first + second
print(sum)

#7

a = 'Abraham John x'

print(a.upper())                                                      #STRING TO UPPERCASE
print(a.lower())                                                      #STRING TO LOWERCASE
print(a.find('a'))                                                    #finds position of alphabets
print(a.replace('x' , 'Elias'))                                       #replaces words
print('John' in a)

#8

print(10+3)                                                           #addition
print(10-3)                                                           #subtraction
print(10*3)                                                           #multiplication
print(10/3)                                                           #division (gives in float)
print(10//3)                                                          #division (gives in int)
print(10%3)                                                           #remainder
print(10**3)                                                          #power

x = 10
x = x + 3
print(x)
#OR 
x = 10
x += 3
x -= 3
x *= 3
x /= 3
x //=3  
print(x)

#9

price = 25    
print(price>10)                                                      #true
print(price>10 and price<30)                                         # Both are true = true
print(price>10 or price<1)                                           #if one is true = true
print(price<1)                                                       #false
print(price<1 and price>10)                                          #if one is false = false
print(price<1 or price>10)                                           #if one is true = true
print(not price<1)                                                   #converts true to false or vice-versa

#10

temperature = int(input("Enter the temperature.\n"))

if temperature >= 30 :
    print("It's a hot day")
elif temperature >= 20:
    print("It's a nice day ")
elif temperature >= 15:
    print("It's a bit cold")
else:
    print("It's Cold") 

a = float(input("Enter weight.\n"))
b = (input(" (K)gs or (L)bs : "))
if b == "K":
    c = a / 0.45
    print("Weight in Lbs :" , c)
else:
    c = a * 0.45
    print("Weight in Kgs : " , c)

#11

from re import U


i = 1    
while i <= 50:
    print(i * '*') 
    i = i + 1

#12

names = ["John" , "Tani" , "Las" , "Mosh" , "DIK"]
names[0] = "Abraham"
print(names[0:3])

a = [1,2,3,4,5] 
a.append(6)

b = [1,2,3,4,5]
b.insert(0, 0)
b.remove(5)
print(b)
print(2 in b )
print(7 in b )
print(len(b))

#13

a = [1,2,3,4,5] 
for i in a:
    print(i)

#14

a = range(5, 10)
for i in a:g
    print(i)

for i in range(5 , 15 ,2):
    print(i)

#15

a = (1,2,3,4,5)

import re


def hello_function():
    print("yeet")

hello_function()  

def area(l,b):
    area = l*b
    return area
    
area(50,50)

'''
