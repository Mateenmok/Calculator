ask = int(input("[1] Finance Calculator\n[2] Mortgage Calculator\n[3] Standard Calculator\n"))
if ask == 1:
    # COMPOUND INTEREST CALCULATOR
    mortgage = float(input("Enter your current balance "))
    # Asks the user what their current balance is
    years = int(input("How many years are you paying interest? "))
    # Asks the user how many years they have on their mortgage
    interest = float(input("What is your current interest percentage? "))
    # Asks the user what their current interest rate is
    b = (mortgage * (1 + interest/100) ** years)
    #
    print(b)
if ask == 2:
    # MONTHLY MORTGAGE PAYMENTS CALCULATOR
    principal = float(input("Enter the current amount of your loan "))
    # Asks the user how much they have left on their loan
    print(principal)
    # Prints the loan
    intrate = float(input("Enter your current interest rate "))
    #  Collects input from user that gets their interest rate
    print(intrate)
    # Prints the interest rate
    length = int(input("Enter the amount of years left on your loan "))

    print("Your compound interest is.. ", length)
    month = length * 12
    month_interest = float(intrate/(12 * 100))


    print(1-(1+month_interest)**(-month))
    month_payment = principal*(month_interest/(1-(1+month_interest)**(-month)))

    print("Your monthly mortgage payment is.. ",month_payment)

# Python program to  create a simple GUI
# calculator using Tkinter
if ask == 3:
    # Gives user the option of 3 themes, by entering 1, 2, or 3
    ask2 = int(input(" THEMES:\n[1] Blue/Purple\n[2] Orange/Red\n[3] Green/Yellow\n"))
    # If the user selects 1 they get the Blue/Purple Calculator
    if ask2 == 1:
        from tkinter import *
        # Imports tkinter which allows us to use a gui

        expression = ""

        # Function to update expression
        def press(num):
            global expression
            # concatenation of string
            expression = expression + str(num)
            equation.set(expression)


        # Function to evaluate the final expression
        def equalpress():
            try:
                # Try and except statement is used
                # for handling the errors like zero
                global expression

                total = str(eval(expression))

                equation.set(total)

                expression = ""

            except:

                equation.set(" error ")
                expression = ""


        # Function to clear the contents
        # of text entry box

        def clear():
            global expression
            expression = ""
            equation.set("")


        if __name__ == "__main__":
            gui = Tk()
            # Style and formatting options for Calculator GUI
            gui.configure(background="black")

            gui.title("Simple Calculator")

            gui.geometry("265x125")

            equation = StringVar()

            expression_field = Entry(gui, textvariable=equation)

            expression_field.grid(columnspan=4, ipadx=70)

            equation.set('enter your expression')

            button1 = Button(gui, text=' 1 ', fg='black', bg='blue',
                    command=lambda: press(1), height=1, width=7)
            button1.grid(row=2, column=0)

            button2 = Button(gui, text=' 2 ', fg='black', bg='purple',
                    command=lambda: press(2), height=1, width=7)
            button2.grid(row=2, column=1)

            button3 = Button(gui, text=' 3 ', fg='black', bg='blue',
                    command=lambda: press(3), height=1, width=7)
            button3.grid(row=2, column=2)

            button4 = Button(gui, text=' 4 ', fg='black', bg='purple',
                    command=lambda: press(4), height=1, width=7)
            button4.grid(row=3, column=0)

            button5 = Button(gui, text=' 5 ', fg='black', bg='blue',
                    command=lambda: press(5), height=1, width=7)
            button5.grid(row=3, column=1)

            button6 = Button(gui, text=' 6 ', fg='black', bg='purple',
                    command=lambda: press(6), height=1, width=7)
            button6.grid(row=3, column=2)

            button7 = Button(gui, text=' 7 ', fg='black', bg='blue',
                    command=lambda: press(7), height=1, width=7)
            button7.grid(row=4, column=0)

            button8 = Button(gui, text=' 8 ', fg='black', bg='purple',
                    command=lambda: press(8), height=1, width=7)
            button8.grid(row=4, column=1)

            button9 = Button(gui, text=' 9 ', fg='black', bg='blue',
                    command=lambda: press(9), height=1, width=7)
            button9.grid(row=4, column=2)

            button0 = Button(gui, text=' 0 ', fg='black', bg='purple',
                    command=lambda: press(0), height=1, width=7)
            button0.grid(row=5, column=0)

            plus = Button(gui, text=' + ', fg='black', bg='purple',
                    command=lambda: press("+"), height=1, width=7)
            plus.grid(row=2, column=3)

            minus = Button(gui, text=' - ', fg='black', bg='blue',
                    command=lambda: press("-"), height=1, width=7)
            minus.grid(row=3, column=3)

            multiply = Button(gui, text=' * ', fg='black', bg='purple',
                    command=lambda: press("*"), height=1, width=7)
            multiply.grid(row=4, column=3)

            divide = Button(gui, text=' / ', fg='black', bg='blue',
                    command=lambda: press("/"), height=1, width=7)
            divide.grid(row=5, column=3)

            equal = Button(gui, text=' = ', fg='black', bg='purple',
                    command=equalpress, height=1, width=7)
            equal.grid(row=5, column=2)

            clear = Button(gui, text='Clear', fg='black', bg='blue',
                    command=clear, height=1, width=7)
            clear.grid(row=5, column='1')

            # start the GUI
            gui.mainloop()
    # If the user inputs 2, they get the Orange/Red Calculator
    if ask2 == 2:
        from tkinter import *

        expression = ""


        def press(num):
            global expression

            expression = expression + str(num)
            equation.set(expression)


        def equalpress():
            try:

                global expression

                total = str(eval(expression))

                equation.set(total)

                expression = ""

            except:

                equation.set(" error ")
                expression = ""


        def clear():
            global expression
            expression = ""
            equation.set("")


        if __name__ == "__main__":
            gui = Tk()

            gui.configure(background="black")

            gui.title("Simple Calculator")

            gui.geometry("265x125")

            equation = StringVar()

            expression_field = Entry(gui, textvariable=equation)

            expression_field.grid(columnspan=4, ipadx=70)

            equation.set('enter your expression')

            button1 = Button(gui, text=' 1 ', fg='black', bg='orange',
                    command=lambda: press(1), height=1, width=7)
            button1.grid(row=2, column=0)

            button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                    command=lambda: press(2), height=1, width=7)
            button2.grid(row=2, column=1)

            button3 = Button(gui, text=' 3 ', fg='black', bg='orange',
                    command=lambda: press(3), height=1, width=7)
            button3.grid(row=2, column=2)

            button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                    command=lambda: press(4), height=1, width=7)
            button4.grid(row=3, column=0)

            button5 = Button(gui, text=' 5 ', fg='black', bg='orange',
                    command=lambda: press(5), height=1, width=7)
            button5.grid(row=3, column=1)

            button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                    command=lambda: press(6), height=1, width=7)
            button6.grid(row=3, column=2)

            button7 = Button(gui, text=' 7 ', fg='black', bg='orange',
                    command=lambda: press(7), height=1, width=7)
            button7.grid(row=4, column=0)

            button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                    command=lambda: press(8), height=1, width=7)
            button8.grid(row=4, column=1)

            button9 = Button(gui, text=' 9 ', fg='black', bg='orange',
                    command=lambda: press(9), height=1, width=7)
            button9.grid(row=4, column=2)

            button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                    command=lambda: press(0), height=1, width=7)
            button0.grid(row=5, column=0)

            plus = Button(gui, text=' + ', fg='black', bg='red',
                    command=lambda: press("+"), height=1, width=7)
            plus.grid(row=2, column=3)

            minus = Button(gui, text=' - ', fg='black', bg='orange',
                    command=lambda: press("-"), height=1, width=7)
            minus.grid(row=3, column=3)

            multiply = Button(gui, text=' * ', fg='black', bg='red',
                    command=lambda: press("*"), height=1, width=7)
            multiply.grid(row=4, column=3)

            divide = Button(gui, text=' / ', fg='black', bg='orange',
                    command=lambda: press("/"), height=1, width=7)
            divide.grid(row=5, column=3)

            equal = Button(gui, text=' = ', fg='black', bg='red',
                    command=equalpress, height=1, width=7)
            equal.grid(row=5, column=2)

            clear = Button(gui, text='Clear', fg='black', bg='orange',
                    command=clear, height=1, width=7)
            clear.grid(row=5, column='1')

            # start the GUI
            gui.mainloop()
    # If user inputs 3 they get the Yellow/Green Calculator
    if ask2 == 3:
        from tkinter import *

        expression = ""


        def press(num):
            global expression

            expression = expression + str(num)
            equation.set(expression)


        def equalpress():
            try:

                global expression

                total = str(eval(expression))

                equation.set(total)

                expression = ""

            except:

                equation.set(" error ")
                expression = ""


        def clear():
            global expression
            expression = ""
            equation.set("")


        if __name__ == "__main__":
            gui = Tk()

            gui.configure(background="black")

            gui.title("Simple Calculator")

            gui.geometry("265x125")

            equation = StringVar()

            expression_field = Entry(gui, textvariable=equation)

            expression_field.grid(columnspan=4, ipadx=70)

            equation.set('enter your expression')

            button1 = Button(gui, text=' 1 ', fg='black', bg='yellow',
                             command=lambda: press(1), height=1, width=7)
            button1.grid(row=2, column=0)

            button2 = Button(gui, text=' 2 ', fg='black', bg='green',
                             command=lambda: press(2), height=1, width=7)
            button2.grid(row=2, column=1)

            button3 = Button(gui, text=' 3 ', fg='black', bg='yellow',
                             command=lambda: press(3), height=1, width=7)
            button3.grid(row=2, column=2)

            button4 = Button(gui, text=' 4 ', fg='black', bg='green',
                             command=lambda: press(4), height=1, width=7)
            button4.grid(row=3, column=0)

            button5 = Button(gui, text=' 5 ', fg='black', bg='yellow',
                             command=lambda: press(5), height=1, width=7)
            button5.grid(row=3, column=1)

            button6 = Button(gui, text=' 6 ', fg='black', bg='green',
                             command=lambda: press(6), height=1, width=7)
            button6.grid(row=3, column=2)

            button7 = Button(gui, text=' 7 ', fg='black', bg='yellow',
                             command=lambda: press(7), height=1, width=7)
            button7.grid(row=4, column=0)

            button8 = Button(gui, text=' 8 ', fg='black', bg='green',
                             command=lambda: press(8), height=1, width=7)
            button8.grid(row=4, column=1)

            button9 = Button(gui, text=' 9 ', fg='black', bg='yellow',
                             command=lambda: press(9), height=1, width=7)
            button9.grid(row=4, column=2)

            button0 = Button(gui, text=' 0 ', fg='black', bg='green',
                             command=lambda: press(0), height=1, width=7)
            button0.grid(row=5, column=0)

            plus = Button(gui, text=' + ', fg='black', bg='green',
                          command=lambda: press("+"), height=1, width=7)
            plus.grid(row=2, column=3)

            minus = Button(gui, text=' - ', fg='black', bg='yellow',
                           command=lambda: press("-"), height=1, width=7)
            minus.grid(row=3, column=3)

            multiply = Button(gui, text=' * ', fg='black', bg='green',
                              command=lambda: press("*"), height=1, width=7)
            multiply.grid(row=4, column=3)

            divide = Button(gui, text=' / ', fg='black', bg='yellow',
                            command=lambda: press("/"), height=1, width=7)
            divide.grid(row=5, column=3)

            equal = Button(gui, text=' = ', fg='black', bg='green',
                           command=equalpress, height=1, width=7)
            equal.grid(row=5, column=2)

            clear = Button(gui, text='Clear', fg='black', bg='yellow',
                           command=clear, height=1, width=7)
            clear.grid(row=5, column='1')

            # start the GUI
            gui.mainloop()