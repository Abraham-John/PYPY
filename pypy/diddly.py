import smtplib


print ("Hello Diddlies")

a = int(input("Enter Age.\n"))
if a>= 15 and a<=47 :
    print("Eligible to vote") 
    print("NOW YOU ARE THE PART OF THE DIDDLY CULT.\n" *10)
    
elif a>47:
    print("Diddly overused. UNABLE TO JOIN CULT\n")

else :
    print("Not Eligible") 
    print("YOUR DIDDLY IS DIMINUTIVE.\n" *10)