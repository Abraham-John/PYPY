a = list("hello world")
b = list("abcdefghijklmnopqrstuvwxyz")
c = ""
for i in a:
    for j in b:
        print(c+j)
        if i==j:
            c=c+j
            break

