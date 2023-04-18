from tkinter import *

window = Tk()
window.title("EMMAPP CALCULATOR")
window.geometry("325x460")
window["bg"] = "grey"
window.resizable(False, False)

top_frame = Frame(window)
top_frame.pack(padx=10, pady=10)

input_text = StringVar()

screen = Entry(top_frame, justify=RIGHT, width=30, font=("Arial", 20), textvariable=input_text)
screen.pack()
ans_display = Label(top_frame, justify=RIGHT, width=30, font=("Arial", 15, "bold"))
ans_display.pack(side=BOTTOM)

expression = ""


#  function to display items on entry screen
def press(buttons):
    global expression
    expression = expression + str(buttons)
    input_text.set(expression)


#   function to clear the entry screen
def clearscreen():
    global expression
    expression = ""
    input_text.set("")


#   function to evaluate the expressions on the entry screen
def equals_button():
    global expression
    try:
        result = str(eval(expression))
        ans_display.config(text=result)
    except ZeroDivisionError:
        ans_display.config(text="Division by zero not possible")


#   function to clear the answer label
def clear_label():
    ans_display.config(text="")


#   backspace button
def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)


button_one = Button(window, text="1", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                    command=lambda: press(1))
button_two = Button(window, text="2", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                    command=lambda: press(2))
button_three = Button(window, text="3", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                      command=lambda: press(3))
button_four = Button(window, text="4", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                     command=lambda: press(4))
button_five = Button(window, text="5", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                     command=lambda: press(5))
button_six = Button(window, text="6", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                    command=lambda: press(6))
button_seven = Button(window, text="7", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                      command=lambda: press(7))
button_eight = Button(window, text="8", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                      command=lambda: press(8))
button_nine = Button(window, text="9", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                     command=lambda: press(9))
button_zero = Button(window, text="0", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                     command=lambda: press(0))
button_plus = Button(window, text="+", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                     command=lambda: press("+"))
button_minus = Button(window, text="-", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                      command=lambda: press("-"))
button_mult = Button(window, text="x", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                     command=lambda: press("*"))
button_divide = Button(window, text="/", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                       command=lambda: press("/"))
button_equals = Button(window, text="=", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                       command=lambda: equals_button())
button_clear = Button(window, text="clear", relief=RAISED, bg="silver", width=4, height=2, font=("Verdana", 15, "bold"),
                      command=lambda: [clearscreen(), clear_label()])
button_bkspc = Button(window, text="BKSPC", relief=RAISED, bg="silver", width=4, height=1,
                      font=("Verdana", 7, "italic"), command=lambda: backspace())

button_seven.place(x=20, y=100)
button_eight.place(x=90, y=100)
button_nine.place(x=160, y=100)
button_plus.place(x=230, y=100)
button_four.place(x=20, y=180)
button_five.place(x=90, y=180)
button_six.place(x=160, y=180)
button_minus.place(x=230, y=180)
button_one.place(x=20, y=260)
button_two.place(x=90, y=260)
button_three.place(x=160, y=260)
button_mult.place(x=230, y=260)
button_clear.place(x=20, y=340)
button_zero.place(x=90, y=340)
button_equals.place(x=160, y=340)
button_divide.place(x=230, y=340)
button_bkspc.place(x=20, y=420)

bottom_label = Label(window, text="Designed by EMMAPP", bg="gray", fg="blue", font=("Chiller", 11, "bold"))
bottom_label.place(x=100, y=420)


window.mainloop()
