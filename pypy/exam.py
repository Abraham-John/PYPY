'''m = int(input("ENter a number "))
n = int(input("ENter 2nd number "))
primeCount = 0
for i in range(m,n+1):
    count =  0
    for j in range(1 , i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
        primeCount += 1
print("total prime numbers = ", primeCount)'''


'''str1 = input(("Enter a string.\n"))
str2 = str1[::-1]
if (str1==str2):
    print("Its a palindrome")
else:
    print("Not palindrome")'''

'''str1 = input(("Enter a string.\n"))
str2 = str1[::-1]
print(str2)'''

'''a = 'Amazing dic game'
sub = "e"

b = a.find(sub)
print(b)
'''
'''a = {"tani": "gay for me" , "garu" : "tani", "hi" : "john" , "me" : "is hot af"}
print(a["hi"] , a["me"] , "and",a["garu"] ,"is", a["tani"] )'''


l1 = [1,5,66,4]
l1.sort(reverse=True)
print(l1)