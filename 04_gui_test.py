from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image



######### LOGO
#tk_image = PhotoImage(file="https://www.remove.bg/")
#image_label = ttk.Label(root, image=tk_image)
#image_label.place(relx=0.1, rely=0.0)
#style = ttk.Style()

################################ FIRST WINDOW ################################
def main_window():
    root = Tk()
    root.title("Find and Dine")
    root.geometry('600x800')

    top_frame = ttk.Label(main_window, text='Find and Dine', font=('Helvetica, 21'))
    intro_search_button = Button(main_window, text='Search', height= 2, command=open_search_window, font=('Helvetica, 20'))
    top_frame.place(relx=0.5, rely=0.65, anchor='center')
    intro_search_button.place(relx=0.25, rely=0.7, relwidth=0.5)
################################ SECOND WINDOW ################################
    def open_search_window():
        search_window = Tk()
        search_window.title("Find and Dine")
        search_window.geometry('600x800')
        root.destroy()
    # BACK BUTTON COMMAND
        def back_btn():
            search_window.destroy()
            main_window()
        back_button = Button(search_window, text="Back", width= 5, command=back_btn)
        back_button.place(relx=0.45, rely=0.95)
    # SEARCH BUTTON OPENS A NEW WINDOW THAT SHOWS THE NEAREST RESTAURANTS
        def search_again():
                third_window = Tk()
                third_window.title("Find and Dine")
                third_window.geometry("600x800")
                open_search_window.destroy()

                def back_btn_2():
                    third_window.destroy()
                    search_window()
                back_button

        ##### INPUT FIELD
        latitude_label = Label(search_window, foreground='white', font=('Helvetica, 12'), text="Latitude:")
        latitude_label.place(relx=0.05, rely=0.01, anchor='nw')
        lat_input = Entry(search_window, foreground='white', font=('Helvetica, 12'))
        lat_input.place(relx=0.05, rely=0.03, anchor='nw', relwidth=0.25)

        longitude_label = Label(search_window, foreground='white', font=('Helvetica, 12'), text="Longitude:")
        longitude_label.place(relx=0.32, rely=0.01, anchor='nw')
        lon_input = Entry(search_window, foreground='white', font=('Helvetica, 12'))
        lon_input.place(relx=0.32, rely=0.03, anchor='nw', relwidth=0.25)
        ##### SEARCH BUTTON 
        coord_search_button = Button(search_window, text="Search", font=('Helvetica, 12'), command=search_again)
        coord_search_button.place(relx=0.7, rely=0.03, relwidth=0.2)
    ##################
        ##### FAST FOOD PLACE - RANKED BASED ON RATIINGS
        first_fastf = Label(search_window, background='light grey', foreground='black', text="first", )
        first_fastf.place(relx=0.0, rely=0.098, relwidth=1.0, relheight=0.2)
        second_fastf = Label(search_window, background='light grey', foreground='black', text="second")
        second_fastf.place(relx=0.0, rely=0.31, relwidth=1.0, relheight=0.2)
        third_fastf = Label(search_window, background='light grey', foreground='black', text="third")
        third_fastf.place(relx=0.0, rely=0.523, relwidth=1.0, relheight=0.2)
        fourth_fastf = Label(search_window, background='light grey', foreground='black', text="fourth")
        fourth_fastf.place(relx=0.0, rely=0.735, relwidth=1.0, relheight=0.2)



main_window()


#class User():
