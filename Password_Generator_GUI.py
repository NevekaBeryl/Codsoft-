from tkinter import *
from tkinter import ttk
import random,string

root = Tk()
root.title("Password Generator")
root.geometry("600x600")
out = StringVar()

def pw_generator():
    lenpi = int(len.get())
    letters =  string.ascii_letters
    numbers = string.digits
    spl_chars = string.punctuation
    char = (letters+numbers+spl_chars)
    pw =  "".join(random.sample(char,lenpi))
    out.set(pw)

def reset_fields():
    txt.delete(0, END)  
    len.delete(0, END)  
    out.set("") 

heading = Label(root, font=('bold', 15), text='Generate Password',fg = "blue")
heading.place(x = 220, y= 50)


name = Label(root,font = ("Times new roman",12),text = "Enter user name : ")
name.place(x = 150,y = 180)
txt = Entry(root, width=25)
txt.place(relx = 0.5, rely = 0.3)


pw_len = Label(root,font = ("Times new roman",12),text = "Enter password length : ")
pw_len.place(x = 150,y = 220)
len = Entry(root, width=25)
len.place(relx = 0.5, rely = 0.37)


pw = Label(root,font = ("Times new roman",12),text  = "Generate :",)
pw.place(x=150,y=260)
gene = Entry(root, width=25,textvariable = out)
gene.place(relx = 0.5, rely = 0.44)

Button_gene = ttk.Button(root,text = "Generate password",command = pw_generator)
Button_gene.place(x = 250,y = 360)

Button_reset = ttk.Button(root,text = "Reset",command = reset_fields)
Button_reset.place(x=265,y = 400)

Button_accept = ttk.Button(root,text = "Accept",command=lambda: root.quit())
Button_accept.place(x = 265,y = 440)

root.mainloop()

