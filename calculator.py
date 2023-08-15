from tkinter import *

# when a number or operator button is pressed. 
# It appends the pressed number/operator to the eq_text string and updates the display on the calculator
def pressbutton(num):
    global eq_text
    eq_text = eq_text +  str(num)
    eq_label.set(eq_text)

# when the equal button is pressed. It evaluates the expression stored in eq_text using the eval function and displays the result.
def equal():
    global eq_text

    try:
        total = str(eval(eq_text))
        eq_label.set(total)
        eq_text = total
    except SyntaxError:
        eq_label.set("Syntax error")
        eq_text = ''
    except ZeroDivisionError:
        eq_label.set("Arithmetic error")
        eq_text = ''

# when the AC (All Clear) button is pressed. It clears the current equation and resets the display
def clear():
    global eq_text
    eq_label.set("")
    eq_text = ""

#  when the backspace button (C) is pressed. It removes the last character from the eq_text string and updates the display.
def backspace():
    global eq_text
    eq_text = eq_text[:-1]
    eq_label.set(eq_text)

# when the +/- button is pressed. It changes the sign of the current number in the eq_text string.
def sign():
    global eq_text
    if eq_text and eq_text[0] != '-':
        eq_text = '-' + eq_text
    elif eq_text and eq_text[0] == '-':
        eq_text = eq_text[1:]
    eq_label.set(eq_text)


root = Tk()
root.geometry('325x490')
root.title("CALCULATOR")
root.config(background="white")
eq_text = ""
eq_label = StringVar()

standard = Label(root,text = 'Standard',font = ('Arial',12),fg = 'black',height = 2,width = 24)
standard.pack()

# creates the main display area of the calculator where the equation is displayed using the eq_label variable.
label = Label(root, 
              textvariable = eq_label, 
              font = ("Arial",20),
              bg = "white",
              width = 24,
              height = 4
              )
label.pack()

# A frame is created to hold the buttons in the calculator interface.
frame = Frame(root)
frame.pack()

# The subsequent lines of code create various buttons for digits, operators, and functions and place them in a grid layout within the frame.
clear_ = Button(frame,text = 'AC',height = 2,width = 6,font = ('Arial',14,'bold'),fg = 'blue', command = clear,bg = 'white')
clear_.grid(row = 0,column = 0)

button_back = Button(frame,text = 'C',height = 2,width = 6,font = ('Arial',14,'bold'),fg = 'blue', command = backspace,bg = 'white')
button_back.grid(row = 0,column = 1)

button_sign = Button(frame,text = '+/-',height = 2,width = 6,font = ('Arial',14,'bold'),fg = 'blue', command = sign,bg = 'white')
button_sign.grid(row = 0,column = 2)

divide = Button(frame,text = '/',height = 2,width = 6,font = ('Arial',14,'bold'),fg = 'blue', command = lambda:pressbutton('/'),bg = 'white')
divide.grid(row = 0,column = 3)

button_7 = Button(frame,text = '7',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton(7),bg = 'white')
button_7.grid(row = 1,column = 0)

button_8 = Button(frame,text = '8',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton(8),bg = 'white')
button_8.grid(row = 1,column = 1)

button_9 = Button(frame,text = '9',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton(9),bg = 'white')
button_9.grid(row = 1,column = 2)

multiply = Button(frame,text = '*',height = 2,width = 6,font = 35,fg = 'blue', command =lambda: pressbutton('*'),bg = 'white')
multiply.grid(row = 1,column = 3)

button_4 = Button(frame,text = '4',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton(4),bg = 'white')
button_4.grid(row = 2,column = 0)

button_5 = Button(frame,text = '5',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton(5),bg = 'white')
button_5.grid(row = 2,column = 1)

button_6 = Button(frame,text = '6',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton(6),bg = 'white')
button_6.grid(row = 2,column = 2)

minus = Button(frame,text = '-',height = 2,width = 6,font = 35,fg = 'blue', command =lambda: pressbutton('-'),bg = 'white')
minus.grid(row = 2,column = 3)

button_1 = Button(frame,text = '1',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton(1),bg = 'white')
button_1.grid(row = 3,column = 0)

button_2 = Button(frame,text = '2',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton(2),bg = 'white')
button_2.grid(row = 3,column = 1)

button_3 = Button(frame,text = '3',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton(3),bg = 'white')
button_3.grid(row = 3,column = 2)

plus = Button(frame,text = '+',height = 2,width = 6,font = 35,fg = 'blue', command = lambda:pressbutton('+'),bg = 'white')
plus.grid(row = 3,column = 3)

button_0 = Button(frame,text = '0',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton(0),bg = 'white')
button_0.grid(row = 4,column = 1)

percentage = Button(frame,text = '%',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton('%'),bg = 'white')
percentage.grid(row = 4,column = 0)

decimal = Button(frame,text = '.',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = lambda:pressbutton('.'),bg = 'white')
decimal.grid(row = 4,column = 2)

equal_ = Button(frame,text = '=',height = 2,width = 6,font = ('Arial',14,'bold'),fg ='black', command = equal,bg = 'white')
equal_.grid(row = 4,column = 3)

root.mainloop()
