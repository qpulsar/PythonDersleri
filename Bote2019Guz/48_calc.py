from tkinter import *

def topla():
    s3.set(str(int(s1.get())+int(s2.get())))
def cikart():
    s3.set(str(int(s1.get())-int(s2.get())))
def carp():
    s3.set(str(int(s1.get())*int(s2.get())))
def bol():
    s3.set(str(int(s1.get())/int(s2.get())))

root = Tk()
root.title("Diyalog penceresi")
root.geometry("300x300-50+10")
s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
Entry(textvariable=s1).pack()
Entry(textvariable=s2).pack()
f = Frame(root)
Button(f, text="+", command=topla).pack(side=LEFT)
Button(f, text="-", command=cikart).pack(side=LEFT)
Button(f, text="*", command=carp).pack(side=LEFT)
Button(f, text="/", command=bol).pack(side=LEFT)
f.pack()
Label(textvariable=s3).pack()
root.mainloop()