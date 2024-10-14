import math

# Class to store lat and lon
class LocationCoord:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

# Class to store restaurant name and location
class FastFoodRestaurant:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.location = LocationCoord(latitude, longitude)

# Formula to calculate distance between two points
class CalculationOfTwoPoints:
    rad_earth = 6371.0  # Radius of Earth in KM

    @staticmethod
    def haversine(pointA, pointB):
        lat1_rad = math.radians(pointA.latitude)
        lon1_rad = math.radians(pointA.longitude)
        lat2_rad = math.radians(pointB.latitude)
        lon2_rad = math.radians(pointB.longitude)

        diff_lat = lat2_rad - lat1_rad
        diff_lon = lon2_rad - lon1_rad

        a = math.sin(diff_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(diff_lon / 2) ** 2
        b = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = CalculationOfTwoPoints.rad_earth * b
        return distance

# Class that finds the four nearest fast food restaurants
class FastFoodFinder:
    def __init__(self, fastf_restaurants):
        self.fastf_restaurants = fastf_restaurants

    def find_four_nearest(self, user_coord, num_nearest=4):
        distances = []
        for restaurant in self.fastf_restaurants:  # Fixed typo here
            distance = CalculationOfTwoPoints.haversine(user_coord, restaurant.location)
            distances.append((restaurant.name, distance))

        # Sort the restaurants by distance from user
        distances.sort(key=lambda x: x[1])
        return [distances[i][0] for i in range(min(num_nearest, len(distances)))]

# Function to get user coordinates with validation
def get_user_coord():
    while True:
        try:
            # Prompt user for latitude and longitude
            lat = float(input("Enter your coordinate's Latitude: "))
            lon = float(input("Enter your coordinate's Longitude: "))

            # Check if they are within valid ranges
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                return LocationCoord(lat, lon)
            else:
                print("Coordinates are out of range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Sample fast food locations
fastf_locs = [
    FastFoodRestaurant("Birdy Bytes \n Ratings: 4.7 / 5", -36.91540360714608, 174.87203796632136),
    FastFoodRestaurant("Burger Fuel \n Ratings: 4.5 / 5", -36.9107909781057, 174.87174736090853),
    FastFoodRestaurant("Subway \n Ratings: 3.8 / 5", -36.91268903482884, 174.87155663683762),
    FastFoodRestaurant("Mcdonalds \n Ratings: 3.3 / 5", -36.89963910924124, 174.90058447864246),
    FastFoodRestaurant("Mighty Hotdog \n Ratings: 4.4 / 5", -36.9123325342632, 174.87065238555024),
    FastFoodRestaurant("Ok Chiken \n Ratings: 4.5 / 5", -36.91225777477972, 174.87061862899873),
    FastFoodRestaurant("Pakuranga Pizza \n Ratings: 4.5 / 5", -36.9153257155152, 174.88970536578574),
    FastFoodRestaurant("Noodle Canteen \n Ratings: 3.8 / 5", -36.912581675641114, 174.87078515794573),
    FastFoodRestaurant("KFC \n Ratings: 2.9 / 5", -36.9003865591953, 174.89939711340074),
    FastFoodRestaurant("Porterhouse Grill \n Ratings: 4.3 / 5", -36.912464364020884, 174.8723767088602)
]

# Function to calculate dinstance from user to each fast food restauran

def calculate_distance(user_coord, fastf_locs):
    print("\nDistance from your location to each fast food restaurant: ")
    for restaurant in fastf_locs:
        distance = CalculationOfTwoPoints.haversine(user_coord, restaurant.location)
        print(f"{restaurant.name}: {distance:.2f} km")

# Get user coordinates
user_coord = get_user_coord()

# Calculate and show distances
calculate_distance(user_coord, fastf_locs)
