'''str1 = input(("Enter a string.\n"))
a=l=u=d=c=v=s=0

for i in range(len(str1)):
    if(str1[i].isupper()):
        u=u+1
    if(str1[i].islower()):
        l=l+1
    if(str1[i].isalpha()):
        a=a+1
    if(str1[i].isdigit()):
        d=d+1
    if(str1[i] in "a,e,i,o,u"):
        v=v+1
    if(str1[i] not in "a,e,i,o,u"):
        c=c+1

print("Number of uppercase letters :" , u)
print("Number of lowercase letters :" , l)
print("Number of alphabets letters :" , a)
print("Number of digits letters :" , d)
print("Number of vowel letters :" , v)
print("Number of consonant letters :" , c)'''

'''str1 = input(("Enter a string.\n"))
str2 = str1[::-1]
if (str1==str2):
    print("Its a palindrome")
else:
    print("Not palindrome")'''


'''a = []
b = int(input("How many numbers : "))
for n in range(b):
    c = int(input("Enter number.\n"))
    a.append(c)

print("maximum element : " , max(a))
print("minimum element : " , min(a))'''


a = []
print("Enter the size of list : ")
b = int(input())

print("Enter elements for the list : ")
for i in range(b):
    a.append(input())

print("\nEnter an element to be search : ")
c = input()

for i in range(b):
    if c == a[i]:
        print("\nElement found at Position:", i+1)