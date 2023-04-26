import tkinter as tk
root = tk.Tk()
root.geometry("300x250")

def submit():
    k = 0
    T = -1
    count = 0
    p = palinEntry.get()
    l1 = list(p)
    for i in range(len(p)):
        if p[k] == p[T]:
            count = count+1 
        else:
            print("Not palindrome")

    if count==len(p):
       print("Its a palindrome")


tk.Label(root,text="Enter a Sentence",padx=15,pady=10).grid()

palin = tk.StringVar()
palinEntry = tk.Entry(root,textvariable=palin)
palinEntry.grid(row=0,column=1)

tk.Button(root,text="submit",command=submit).grid(row=5,column=1)

root.mainloop()