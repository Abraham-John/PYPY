k = 0
T = -1
count = 0
p = input("Enter a sentence.\n")
l1 = list(p)
for i in range(len(p)):
    if p[k] == p[T]:
        count = count+1 
    else:
        print("Not palindrome")

if count==len(p):
    print("Its a palindrome")

'''x = input()
p = list(x)
k=0
m=-1
for i in range(len(p)):
    if p[k] == p[m]:
        k+=1
        m-=1
    
    else:
        print("not a palindrome")'''

        
