import math

class LocationCoord:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class FastFoodRestaurant:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.location = LocationCoord(latitude, longitude)

class CalculationOfTwoPoints:
    # Radius of the Earth in KM
    rad_of_earth = 6371.0

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

        distance = CalculationOfTwoPoints.rad_of_earth * b

        return distance

class FastFoodFinder:
    def __init__(self, fast_food_restaurants):
        self.fast_food_restaurants = fast_food_restaurants

    def find_four_nearest(self, user_coord, num_nearest=4):
        distances = []

        for restaurant in self.fast_food_restaurants:
            distance = CalculationOfTwoPoints.haversine(user_coord, restaurant.location)
            distances.append((restaurant, distance))

        distances.sort(key=lambda x: x[1])

        return [distances[i][0] for i in range(min(num_nearest, len(distances)))]

# Example usage
def main():
    # Coordinates of Fast Food Restaurants in Pakuranga
    fast_food_locations = [
        FastFoodRestaurant("Birdy Bytes", -36.91540360714608, 174.87203796632136),
        FastFoodRestaurant("Burger Fuel", -36.9107909781057, 174.87174736090853),
        FastFoodRestaurant("Subway", -36.91268903482884, 174.87155663683762),
        FastFoodRestaurant("McDonald's", -36.89963910924124, 174.90058447864246),
        FastFoodRestaurant("Mighty Hotdog", -36.9123325342632, 174.87065238555024),
        FastFoodRestaurant("Ok Chicken", -36.91225777477972, 174.87061862899873),
        FastFoodRestaurant("Pakuranga Pizza", -36.9153257155152, 174.88970536578574),
        FastFoodRestaurant("Noodle Canteen", -36.912581675641114, 174.87078515794573),
        FastFoodRestaurant("KFC", -36.9003865591953, 174.89939711340074),
        FastFoodRestaurant("Porterhouse Grill", -36.912464364020884, 174.8723767088602)
    ]

    # Initialize FastFoodFinder with the list of restaurants
    finder = FastFoodFinder(fast_food_locations)

    # User location
    user_location = LocationCoord(-36.900191472493795, 174.90017291150596)

    # Find the 4 nearest fast food restaurants
    nearest_restaurants = finder.find_four_nearest(user_location)

    # Print the results
    print("The 4 nearest fast food restaurants are:")
    for restaurant in nearest_restaurants:
        print(f"Restaurant: {restaurant.name}, Location: ({restaurant.location.latitude}, {restaurant.location.longitude})")

if __name__ == "__main__":
    main()
