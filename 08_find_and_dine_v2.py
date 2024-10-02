from tkinter import Tk, Button, Label, Entry, ttk, END
from PIL import Image, ImageTk
import math
import re

# FAST FOOD AND LOCATION CLASSES


class LocationCoord:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


class FastFoodRestaurant:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.location = LocationCoord(latitude, longitude)


class CalculationOfTwoPoints:
    rad_of_earth = 6371.0  # Radius of the Earth in KM

    @staticmethod
    def haversine(pointA, pointB):
        lat1_rad = math.radians(pointA.latitude)
        lon1_rad = math.radians(pointA.longitude)
        lat2_rad = math.radians(pointB.latitude)
        lon2_rad = math.radians(pointB.longitude)

        diff_lat = lat2_rad - lat1_rad
        diff_lon = lon2_rad - lon1_rad

        a = math.sin(diff_lat / 2) ** 2 + math.cos(lat1_rad) * \
            math.cos(lat2_rad) * math.sin(diff_lon / 2) ** 2
        b = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = CalculationOfTwoPoints.rad_of_earth * b
        return distance


class FastFoodFinder:
    def __init__(self, fastf_restaurants):
        self.fastf_restaurants = fastf_restaurants

    def find_four_nearest(self, user_coord, num_nearest=4):
        distances = []
        for restaurant in self.fastf_restaurants:
            distance = CalculationOfTwoPoints.haversine(
                user_coord, restaurant.location)
            distances.append((restaurant.name, distance))

        distances.sort(key=lambda x: x[1])
        return [distances[i][0] for i in range(min(num_nearest, len(distances)))]

# GUI APPLICATION


def main_window():
    root = Tk()
    root.title("Find and Dine")
    root.geometry('600x800')

# LOGO
    image = Image.open('find_and_dine.png')
    image = ImageTk.PhotoImage(image)

    image_label = Label(root, image=image)
    image_label.place(relx=0.08, rely=0.1)

    def validate_coord(user_input):
        """Validate if the input is a valid coordinate (latitude, longitude) and reject integers."""
        if user_input == "":
            return False  # Reject empty input

        # Regular expression to match coordinates in the format "latitude, longitude"
        pattern = r'^[-]?([1-8]?\d(\.\d+)?|90(\.0+)?)\s*,\s*[-]?((1[0-7][0-9]|[1-9]?\d)(\.\d+)?|180(\.0+)?)$'

        if not re.match(pattern, user_input):
            return False

        # Split the input into latitude and longitude
        latitude, longitude = user_input.split(',')

        try:
            lat_float = float(latitude.strip())
            lon_float = float(longitude.strip())

            # Ensure the latitude and longitude contain decimal points
            if '.' not in latitude.strip() or '.' not in longitude.strip():
                return False

            return True
        except ValueError:
            return False

    program_title = ttk.Label(
        root, text='Find and Dine', font=('Helvetica', 26))
    program_subtitle = ttk.Label(root, text='(Pakuranga)', font=('Arial', 18))
    program_title.place(relx=0.5, rely=0.7, anchor='center')
    program_subtitle.place(relx=0.5, rely=0.73, anchor='center')
# Stores the fast food locations name, ratings, and coordinates (latitude, longitude)
    fastf_locs = [
        FastFoodRestaurant("Birdy Bytes \n Ratings: 4.7 / 5", -
                           36.91540360714608, 174.87203796632136),
        FastFoodRestaurant("Burger Fuel \n Ratings: 4.5 / 5", -
                           36.9107909781057, 174.87174736090853),
        FastFoodRestaurant("Subway \n Ratings: 3.8 / 5", -
                           36.91268903482884, 174.87155663683762),
        FastFoodRestaurant("Mcdonalds \n Ratings: 3.3 / 5", -
                           36.89963910924124, 174.90058447864246),
        FastFoodRestaurant("Mighty Hotdog \n Ratings: 4.4 / 5", -
                           36.9123325342632, 174.87065238555024),
        FastFoodRestaurant("Ok Chiken \n Ratings: 4.5 / 5", -
                           36.91225777477972, 174.87061862899873),
        FastFoodRestaurant("Pakuranga Pizza \n Ratings: 4.5 /5", -
                           36.9153257155152, 174.88970536578574),
        FastFoodRestaurant("Noodle Canteen \n Ratings: 3.8 / 5", -
                           36.912581675641114, 174.87078515794573),
        FastFoodRestaurant("KFC \n Ratings: 2.9 / 5", -
                           36.9003865591953, 174.89939711340074),
        FastFoodRestaurant(
            "Porterhouse Grill \n Ratings: 4.3 / 5", -36.912464364020884, 174.8723767088602)
    ]

    fast_food_finder = FastFoodFinder(fastf_locs)

    def open_search_window():
        root.withdraw()  # Hide the main window
        search_window = Tk()
        search_window.title("Find and Dine")
        search_window.geometry('600x800')

        def back_btn():
            search_window.destroy()
            root.deiconify()  # Show the main window again

        back_button = Button(search_window, text="Back",
                             width=5, command=back_btn)
        back_button.place(relx=0.45, rely=0.95)

        def search_again():
            lat = lat_input.get()
            lon = lon_input.get()

            if lat and lon:
                try:
                    # Manually check that latitude and longitude have a decimal point
                    if '.' not in lat or '.' not in lon:
                        raise ValueError("Invalid Coordinate. Try again")

                    lat_float = float(lat)
                    lon_float = float(lon)

                    if not (-90 <= lat_float <= 90) or not (-180 <= lon_float <= 180):
                        raise ValueError("Coordinates out of range")

                    user_coord = LocationCoord(lat_float, lon_float)
                    nearest_restaurants = fast_food_finder.find_four_nearest(
                        user_coord)

                    for label in fastf_labels:
                        label.config(text="")

                    for i, restaurant in enumerate(nearest_restaurants):
                        fastf_labels[i].config(text=f"{i + 1}. {restaurant}")

                except ValueError as e:
                    for label in fastf_labels:
                        label.config(text="")
                    error_label.config(text=str(e))

        def clear_entry():
            lat_input.delete(0, END)
            lon_input.delete(0, END)
            for label in fastf_labels:
                label.config(text="")
            error_label.config(text="")

        # Input Fields
        latitude_label = Label(
            search_window, text="Latitude:", font=('Helvetica', 12))
        latitude_label.place(relx=0.05, rely=0.01, anchor='nw')
        lat_input = Entry(search_window, font=('Helvetica', 12))
        lat_input.place(relx=0.05, rely=0.03, anchor='nw', relwidth=0.25)

        longitude_label = Label(
            search_window, text="Longitude:", font=('Helvetica', 12))
        longitude_label.place(relx=0.32, rely=0.01, anchor='nw')
        lon_input = Entry(search_window, font=('Helvetica', 12))
        lon_input.place(relx=0.32, rely=0.03, anchor='nw', relwidth=0.25)

        coord_search_button = Button(search_window, text="Search", font=(
            'Helvetica', 12), command=search_again)
        coord_search_button.place(relx=0.6, rely=0.03, relwidth=0.2)

        clear_button = Button(search_window, text="Clear", font=(
            'Helvetica', 12), command=clear_entry)
        clear_button.place(relx=0.8, rely=0.03, relwidth=0.1)

        fastf_labels = []
        for i in range(4):
            label = Label(search_window, background='white',
                          foreground='black', text="", font=('Helvetica', 17))
            label.place(relx=0.0, rely=0.1 + i * 0.2,
                        relwidth=1.0, relheight=0.2)
            fastf_labels.append(label)

        for i, restaurant in enumerate(fastf_locs[:4]):
            fastf_labels[i].config(text=f"{i + 1}. {restaurant.name}")

        error_label = Label(search_window, text="", font=(
            'Helvetica', 15), foreground='red')
        error_label.place(relx=0.05, rely=0.90)

    intro_search_button = Button(
        root, text='Search', height=2, command=open_search_window, font=('Helvetica', 20))
    intro_search_button.place(relx=0.25, rely=0.76, relwidth=0.5)

    root.mainloop()


main_window()
