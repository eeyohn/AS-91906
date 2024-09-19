from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image



######### LOGO
#tk_image = PhotoImage(file="https://www.remove.bg/")
#image_label = ttk.Label(root, image=tk_image)
#image_label.place(relx=0.1, rely=0.0)
#style = ttk.Style()

################################ FIRST WINDOW ################################
from tkinter import Tk, Button, Label, Entry, ttk, END

def main_window():
    root = Tk()
    root.title("Find and Dine")
    root.geometry('600x800')

    top_frame = ttk.Label(root, text='Find and Dine', font=('Helvetica', 21))
    top_frame.place(relx=0.5, rely=0.1, anchor='center')

    # Define the search window function outside the main_window function
    def open_search_window():
        root.withdraw()  # Hide the main window
        search_window = Tk()
        search_window.title("Find and Dine")
        search_window.geometry('600x800')

        def back_btn():
            search_window.destroy()
            root.deiconify()  # Show the main window again

        back_button = Button(search_window, text="Back", width=5, command=back_btn)
        back_button.place(relx=0.45, rely=0.95)

        def search_again():
            # Add functionality for searching restaurants here
            pass

        def clear_entry():
            lat_input.delete(0, END)
            lon_input.delete(0, END)

        # Input Fields
        latitude_label = Label(search_window, text="Latitude:", font=('Helvetica', 12))
        latitude_label.place(relx=0.05, rely=0.01, anchor='nw')
        lat_input = Entry(search_window, font=('Helvetica', 12))
        lat_input.place(relx=0.05, rely=0.03, anchor='nw', relwidth=0.25)

        longitude_label = Label(search_window, text="Longitude:", font=('Helvetica', 12))
        longitude_label.place(relx=0.32, rely=0.01, anchor='nw')
        lon_input = Entry(search_window, font=('Helvetica', 12))
        lon_input.place(relx=0.32, rely=0.03, anchor='nw', relwidth=0.25)

        # Search Button
        coord_search_button = Button(search_window, text="Search", font=('Helvetica', 12), command=search_again)
        coord_search_button.place(relx=0.7, rely=0.03, relwidth=0.2)

        clear_button = Button(search_window, text="Clear", font=('Helvetica', 12), command=clear_entry)
        clear_button.place(relx=0.7, rely=0.1, relwidth=0.2)

        # Fast Food Place Labels
        for i in range(4):
            fastf_label = Label(search_window, background='light grey', foreground='black', text=f"{i + 1}. Place {i + 1}")
            fastf_label.place(relx=0.0, rely=0.1 + i * 0.2, relwidth=1.0, relheight=0.2)

    # Button to open search window
    intro_search_button = Button(root, text='Search', height=2, command=open_search_window, font=('Helvetica', 20))
    intro_search_button.place(relx=0.25, rely=0.2, relwidth=0.5)

    root.mainloop()

main_window()




#class User():
