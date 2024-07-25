from tkinter import*
from tkinter import ttk


root = Tk()
root.title("Find and Dine")

# Top Frame
top_frame = ttk.LabelFrame(root, text="Find and Dine")
top_frame.grid(row=0,column=0,padx=5,pady=5,sticky=NSEW)


root.mainloop()