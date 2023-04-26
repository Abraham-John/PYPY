'''a =  input(("Enter a string.\n"))
for i in a:
    print(i,sep="")'''

str1 = input(("Enter a str.\n"))
a=l=u=d=0

for i in range(len(str1)):
    if(str1[i].isupper()):
        u=u+1
    if(str1[i].islower()):
        l=l+1
    if(str1[i].isalnum()):
        a=a+1
    if(str1[i].isdigit()):
        d=d+1

print("Number of uppercase letters :" , u)
print("Number of lowercase letters :" , l)
print("Number of alphabets letters :" , a)
print("Number of digits letters :" , d)

'''st1 = input("Enter a str.\n")
st2 = st1[::-1]
if (st1==st2):
    print("palindrome")
else:
    print("not palindrome")'''

'''lst= []
n = int(input("how many elements.\n"))
for i in range(n):
    a = input("Enter name : ")
    lst.append(a)
print(lst)'''

'''a = [10]
b = a
print(id(a), id(b))'''

a = 'abraham john x'
print(a.replace('x' ,'elias')) 