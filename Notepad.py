from cProfile import label
from tkinter import *

root = Tk()
root.geometry("300x300")
root.title(" Q&A ")
questions = ["what is 2*3", "what is 5*5"]
answers = ["6", "25"]


def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    for i, j in zip(questions, answers):
        if(INPUT == j or "120"):
            Output.insert(END, 'Correct')
            l.config(text=i)
        else:
            Output.insert(END, "Wrong answer")
            break


l = Label(text="What is 24 * 5 ? ")
inputtxt = Text(root, height=10,
                width=25,
                bg="light yellow")

Output = Text(root, height=5,
              width=25,
              bg="light cyan")

Display = Button(root, height=2,
                 width=20,
                 text="Show",
                 command=lambda: Take_input())

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()
