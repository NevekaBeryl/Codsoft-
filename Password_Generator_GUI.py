from tkinter import *
from tkinter import ttk
import random,string

root = Tk()
root.title("Password Generator")
root.geometry("600x600")
root.config(background = '#ffe39f')
out = StringVar()

'''The pw_generator function generates a random password based on the user's input for password length. 
It extracts the desired length from the len Entry widget using len.get()'''
def pw_generator():
    lenpi = int(len.get())
    letters =  string.ascii_letters
    numbers = string.digits
    spl_chars = string.punctuation
    char = (letters+numbers+spl_chars)
    pw =  "".join(random.sample(char,lenpi))
    out.set(pw)

'''The reset_fields function clears the input fields (txt and len Entry widgets) and 
resets the out variable to an empty string, effectively clearing the generated password.'''
def reset_fields():
    txt.delete(0, END)  
    len.delete(0, END)  
    out.set("") 

heading = Label(root, font=('bold', 15), text='Generate Password',fg = "blue")  # display the title "Generate Password"
heading.place(x = 220, y= 50)

'''A label widget name is created to prompt the user to enter their username. 
An Entry widget named txt is provided for the user to input their username.'''
name = Label(root,font = ("Times new roman",12),text = "Enter user name : ") 
name.place(x = 150,y = 180)
txt = Entry(root, width=25)  
txt.place(relx = 0.5, rely = 0.3)

# a label and an Entry widget are created for the user to input the desired password length
pw_len = Label(root,font = ("Times new roman",12),text = "Enter password length : ") # 
pw_len.place(x = 150,y = 220)
len = Entry(root, width=25)
len.place(relx = 0.5, rely = 0.37)


pw = Label(root,font = ("Times new roman",12),text  = "Generate :",)
pw.place(x=150,y=260)
gene = Entry(root, width=25,textvariable = out) # to display the generated password
gene.place(relx = 0.5, rely = 0.44)

#  When clicked, this button calls the pw_generator function to generate a password.
Button_gene = ttk.Button(root,text = "Generate password",command = pw_generator) 
Button_gene.place(x = 250,y = 360)

#  function to clear the input fields and reset the generated password.
Button_reset = ttk.Button(root,text = "Reset",command = reset_fields)
Button_reset.place(x=265,y = 400)

#When clicked, this button uses a lambda function to call root.quit(), which exits the Tkinter main loop and closes the window
Button_accept = ttk.Button(root,text = "Accept",command=lambda: root.quit())
Button_accept.place(x = 265,y = 440)

root.mainloop()

