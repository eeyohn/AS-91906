from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image

##################### FIRST WINDOW ######################
root = Tk()
root.title("Find and Dine")
root.geometry('600x800')

######### LOGO
#tk_image = PhotoImage(file="https://www.remove.bg/")
#image_label = ttk.Label(root, image=tk_image)
#image_label.place(relx=0.1, rely=0.0)
#style = ttk.Style()

##################### SECOND WINDOW ######################
def open_search_window():
    search_window = Tk()
    search_window.title("Find and Dine")
    search_window.geometry('600x800')
    root.destroy()

    ##### INPUT FIELD
    coord_input = Entry(search_window, foreground='white', font=('Helvetica, 12'))
    coord_input.place(relx=0.05, rely=0.03, anchor='nw', relwidth=0.6)
    ##### SEARCH BUTTON 
    coord_search_button = Button(search_window, text="Search", font=('Helvetica, 12'))
    coord_search_button.place(relx=0.7, rely=0.03, relwidth=0.2)
    
    ##### FAST FOOD PLACE - RANKED BASED ON RATIINGS
    first_fastf = Label(search_window, background='light grey', foreground='black', text="Burger King\nburger\nburger", )
    first_fastf.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.2)
    second_fastf = Label(search_window, background='light grey', foreground='black', text="first")
    second_fastf.place(relx=0.0, rely=0.31, relwidth=1.0, relheight=0.2)
    third_fastf = Label(search_window, background='light grey', foreground='black', text="first")
    third_fastf.place(relx=0.0, rely=0.523, relwidth=1.0, relheight=0.2)
    fourth_fastf = Label(search_window, background='light grey', foreground='black', text="first")
    fourth_fastf.place(relx=0.0, rely=0.735, relwidth=1.0, relheight=0.2)

    ##### 

    

######### FUNCTIONS FOR FIRST WINDOW
top_frame = ttk.Label(root, text='Find and Dine', font=('Helvetica, 21'))
intro_search_button = Button(root, text='Search', height= 2, command=open_search_window, font=('Helvetica, 20'))
top_frame.place(relx=0.5, rely=0.65, anchor='center')
intro_search_button.place(relx=0.25, rely=0.7, relwidth=0.5)

root.mainloop()