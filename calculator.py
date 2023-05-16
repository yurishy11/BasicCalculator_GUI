# import the all tkinter for create a simple GUI
import tkinter as tk

# this is the expression variable
calc = ""

# this clears and inserts as the expression forms as the user proceeds
def expression(symbol):
    global calc
    calc += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calc)

def eval_expression():
    global calc
    try:
        result = str(eval(calc))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    # I preferebly do not want to specify all possible errors in the except so i leave generic
    except:
        clear()
        text_result.insert(1.0, "Error in calculation!!")


def clear_expression():
    global calc
    calc = ""
    text_result.delete(1.0, "end")


if __name__ == "__main__":
    # GUI window
    root = tk.Tk()
    # Title
    root.title("Calculator")

    # Size of the window
    root.geometry("350x170")

    # Where the result will be displayed
    text_result = tk.Text(root, height=2, width=24, font=("Arial", 20))
    text_result.grid(columnspan=4)

    button_1 = tk.Button(root, text=' 1 ', fg='black', bg='white',
                    command=lambda: expression(1), height=1, width=12)
    button_1.grid(row=2, column=0)
 
    button_2 = tk.Button(root, text=' 2 ', fg='black', bg='white',
                    command=lambda: expression(2), height=1, width=12)
    button_2.grid(row=2, column=1)
 
    button_3 = tk.Button(root, text=' 3 ', fg='black', bg='white',
                    command=lambda: expression(3), height=1, width=12)
    button_3.grid(row=2, column=2)
 
    button_4 = tk.Button(root, text=' 4 ', fg='black', bg='white',
                    command=lambda: expression(4), height=1, width=12)
    button_4.grid(row=3, column=0)
 
    button_5 = tk.Button(root, text=' 5 ', fg='black', bg='white',
                    command=lambda: expression(5), height=1, width=12)
    button_5.grid(row=3, column=1)
 
    button_6 = tk.Button(root, text=' 6 ', fg='black', bg='white',
                    command=lambda: expression(6), height=1, width=12)
    button_6.grid(row=3, column=2)
 
    button_7 = tk.Button(root, text=' 7 ', fg='black', bg='white',
                    command=lambda: expression(7), height=1, width=12)
    button_7.grid(row=4, column=0)
 
    button_8 = tk.Button(root, text=' 8 ', fg='black', bg='white',
                    command=lambda: expression(8), height=1, width=12)
    button_8.grid(row=4, column=1)
 
    button_9 = tk.Button(root, text=' 9 ', fg='black', bg='white',
                    command=lambda: expression(9), height=1, width=12)
    button_9.grid(row=4, column=2)
 
    button_0 = tk.Button(root, text=' 0 ', fg='black', bg='white',
                    command=lambda: expression(0), height=1, width=12)
    button_0.grid(row=5, column=0)
 
    plus = tk.Button(root, text=' + ', fg='black', bg='white',
                command=lambda: expression("+"), height=1, width=10)
    plus.grid(row=2, column=3)
 
    minus = tk.Button(root, text=' - ', fg='black', bg='white',
                command=lambda: expression("-"), height=1, width=10)
    minus.grid(row=3, column=3)
 
    multiply = tk.Button(root, text=' * ', fg='black', bg='white',
                    command=lambda: expression("*"), height=1, width=10)
    multiply.grid(row=4, column=3)
 
    divide = tk.Button(root, text=' / ', fg='black', bg='white',
                    command=lambda: expression("/"), height=1, width=10)
    divide.grid(row=5, column=3)

    equal = tk.Button(root, text=' = ', fg='black', bg='white',
                command=eval_expression, height=1, width=12)
    equal.grid(row=5, column=2)

    clear = tk.Button(root, text='Clear', fg='black', bg='white',
                command=clear_expression, height=1, width=12)
    clear.grid(row=5, column='1')

    root.mainloop()