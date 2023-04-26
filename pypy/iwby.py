import time
import random

lyrics = ("I just wanna be yours")

alpha = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
a = ""
b=0

while a!= lyrics:
    x=random.randint(0,52)

    if(alpha[x] == lyrics[b]):
        a+=lyrics[b]
        b+=1
        print(a)

    else:
        time.sleep(0.01)
        print(a+alpha[x])


