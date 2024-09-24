from tkinter import Tk, Button, Label, Entry, ttk, END
import math

# FAST FOOD AND LOCATION CLASSES

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

    @staticmethod
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

        distance = Calculation_of_Two_Points.rad_of_earth * b

        return distance
    

class Fast_Food_Finder:
    def __init__(self, fastf_restaurant):
        self.fastf_restaurants = fastf_restaurant

    def find_four_nearest(self, user_coord, num_nearest=4):
        distances = []
        for restaurant in self.fastf_restaurants:
            distance = Calculation_of_Two_Points.haversine(user_coord, restaurant.location)
            distances.append((restaurant.name, distance))
        
        distances.sort(key=lambda x: x[1])
        return [distances[i][0] for i in range(min(num_nearest, len(distances)))]
    

##### GUI APPLICATION

def main_window():
    root = Tk()
    root.title("Find and Dine")
    root.geometry('600x800')

    top_frame = ttk.Label(root, text='Find and Dine', font=('Helvetica', 21))
    top_frame.place(relx=0.5, rely=0.75, anchor='center')

##### Fast Food Locations
    fastf_locs = [ Fast_Food_Restaurant("Birdy Bytes", -36.91540360714608, 174.87203796632136),
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
    
    fast_food_finder = Fast_Food_Finder(fastf_locs)

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
            lat = lat_input.get()
            lon = lon_input.get()

            if lat and lon:
                try:
                    user_coord = Location_coord(float(lat), float(lon))
                    # Find nearest restaurants
                    nearest_restaurants = fast_food_finder.find_four_nearest(user_coord)

                    # Clear previous results and display new results
                    for label in fastf_labels:
                        label.config(text="")

                    for i, restaurant in enumerate(nearest_restaurants):
                        fastf_labels[i].config(text=f"{i + 1}. {restaurant}")

                except ValueError:
                    for label in fastf_labels:
                        label.config(text="")
                    error_label.config(text="Please enter valid coordinates.")

        def clear_entry():
            lat_input.delete(0, END)
            lon_input.delete(0, END)
            for label in fastf_labels:
                label.config(text="")
            error_label.config(text="")

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
        coord_search_button.place(relx=0.6, rely=0.03, relwidth=0.2)

        clear_button = Button(search_window, text="Clear", font=('Helvetica', 12), command=clear_entry)
        clear_button.place(relx=0.8, rely=0.03, relwidth=0.1)

        # Fast Food Place Labels
        fastf_labels = []
        for i in range(4):
            label = Label(search_window, background='light grey', foreground='black', text="")
            label.place(relx=0.0, rely=0.1 + i * 0.2, relwidth=1.0, relheight=0.2)
            fastf_labels.append(label)

        # Pre-fill labels with suggestions
        for i, restaurant in enumerate(fastf_locs[:4]):
            fastf_labels[i].config(text=f"{i + 1}. {restaurant.name}")

        # Error Label
        error_label = Label(search_window, text="", font=('Helvetica', 12), foreground='red')
        error_label.place(relx=0.05, rely=0.85)

    # Button to open search window
    intro_search_button = Button(root, text='Search', height=2, command=open_search_window, font=('Helvetica', 20))
    intro_search_button.place(relx=0.25, rely=0.2, relwidth=0.5)

    root.mainloop()

main_window()
