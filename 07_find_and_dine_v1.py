import math

class Location_coord:
    def __init__(self, latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude


class Fast_Food_Restaurant:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.location = Location_coord(latitude,longitude)


class Calculation_of_Two_Points:
    # Radius of the Earth in KM
    rad_of_earth = 6371.0

    def haversine(pointA, pointB):
        # Calculation of the distance between two points
        # parameter point A: first coordinate
        # parameter point B: second coordinate

        lat1_rad = math.radians(pointA.latitude)
        lon1_rad = math.radians(pointA.longitude)
        lat2_rad = math.radians(pointB.latitude)
        lon2_rad = math.radians(pointB.longitude)

        # Coordinates Difference (Gap between two points)
        diff_lat = lat2_rad - lat1_rad
        diff_lon = lon2_rad - lon1_rad

        # Haversine Formula
        a = math.sin(diff_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(diff_lon / 2)**2
        b = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        # Calculation of the distance between two points in km
        distance = Calculation_of_Two_Points.rad_of_earth * b

        return distance
    
class Fast_Food_Finder():
        def __init__(self, fastf_restaurant):
            self.fastf_restaurants = fastf_restaurant

        def find_four_nearest(self, user_coord, num_nearest=4):
            distances = []

        # Calculation of distandce for each Fast Food Restaurant and storing it in its name
            for FastF in self.fastf_restaurants:
                distance = Calculation_of_Two_Points.haversine(user_coord, Fast_Food_Restaurant.location)
                distances.append(key=lambda x: x[1])

        # Sorts out the fast food restaurants from the first nearest to fourth nearest

            distances.sort(key=lambda x: x[1])

        # Returning the nearerst 'num_nearest' fast food
            return [distances[i][0] for i in range (min(num_nearest, len(distances)))]
        
class Find_and_Dine:
    def __init__(self,root):
        self.root = root
        self.root.title("Find and Dine")

        # Coordinates of Fast Food Restaurants in Pakuranga

        ################# COORDINATES 
        self.fastf_locs = [ Fast_Food_Restaurant("Birdy Bytes", -36.91540360714608, 174.87203796632136),
                       Fast_Food_Restaurant("Burger Fuel", -36.9107909781057,174.87174736090853),
                       Fast_Food_Restaurant("Subway", -36.91268903482884, 174.87155663683762), 
                       Fast_Food_Restaurant("Mcdonalds", -36.89963910924124, 174.90058447864246),
                       Fast_Food_Restaurant("Mighty Hotdog", -36.9123325342632, 174.87065238555024),
                       Fast_Food_Restaurant("Ok Chiken", -36.91225777477972, 174.87061862899873),
                       Fast_Food_Restaurant("Pakuranga Pizza", -36.9153257155152, 174.88970536578574),
                       Fast_Food_Restaurant("Noodle Canteen", -36.912581675641114, 174.87078515794573),
                       Fast_Food_Restaurant("KFC", -36.9003865591953, 174.89939711340074),
                       Fast_Food_Restaurant("Porterhouse Grill", -36.912464364020884, 174.8723767088602)
                       ]
        
        self.loc_finder = Fast_Food_Finder(self.fasf_restaurants)



########## GUI

from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image



######### LOGO
#tk_image = PhotoImage(file="https://www.remove.bg/")
#image_label = ttk.Label(root, image=tk_image)
#image_label.place(relx=0.1, rely=0.0)
#style = ttk.Style()


def main_window():
    root = Tk()
    root.title("Find and Dine")
    root.geometry('600x800')

    def open_search_window():
        search_window = Tk()
        search_window.title("Find and Dine")
        search_window.geometry('600x800')
        root.destroy()
    # BACK BUTTON COMMAND


        def find_nearest_fastf(self):
             try:
                user_lat = float(self.lat_input.get())
                user_lon = float(self.lon_input.get())
                user_location = Location_coord(user_lat, user_lon)
                nearest_fastf = self.loc_finder.find_four_nearest(user_location, num_nearest=4)

                if nearest_fastf:
                  output = "The Nearest Fast Food Restaurants are:\n"
                  for fastfood in nearest_fastf:
                       output += f"- {Fast_Food_Restaurant.__name__}\n"
            
                else:
                  output = "No Fast Food Restaurants near you"
                  self.output.config(text = output)
                
             except ValueError:
                messagebox.showerror("Input Error", "Please enter valid and correct values for latitude and longitude of your coordinates")
                
                
                
                

                
             
        
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
        #coord_search_button = Button(search_window, text="Search", font=('Helvetica, 12'))
        #coord_search_button.place(relx=0.7, rely=0.03, relwidth=0.2)
    ##################
        ##### FAST FOOD PLACE - RANKED BASED ON RATIINGS
        coord_label = Label(search_window, text="", wraplength=400)
        coord_label.place(relx=0.5, rely=0.05)
        
                
    ##### BUTTON BACK TO THE FIRST WINDOW

        # Find button
        search_button = Button(search_window, text="Search", font=('Helvetica, 12'), command=find_nearest_fastf)
        search_button.place(relx=0.7, rely=0.03, relwidth=0.2)
        

    ######### FUNCTIONS
    top_frame = ttk.Label(root, text='Find and Dine', font=('Helvetica, 21'))


    intro_search_button = Button(root, text='Search', height= 2, command=open_search_window, font=('Helvetica, 20'))

    ######### LAYOUT
    top_frame.place(relx=0.5, rely=0.65, anchor='center')
    intro_search_button.place(relx=0.25, rely=0.7, relwidth=0.5)

    root.mainloop()

main_window()


#class User():


    

